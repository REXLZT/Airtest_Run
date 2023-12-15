import pandas as pd
import re
import os


def is_chinese(char):
  """检查字符是否为中文"""
  return '\u4e00' <= char <= '\u9fff'

# 检查字符串中是否含有特殊字符
def has_special_char(s):
  special_chars = "@#￥%……&*（）——+"
    #这里改了波规则，原来的太蛋疼了
  return any(char in special_chars for char in s)

# 提取DetailDesc中的数字
def extract_number_from_detail_desc(detail_desc):
  match = re.search(r'>(\d+)<', detail_desc)   
  #用“><”，可能确实是会有点抽象的，但是用着貌似没啥问题，就先用着吧
  return int(match.group(1)) if match else None

# 检查DetailDesc字段完整性的函数-颜色
def check_detail_desc_integrity(detail_desc):
  pattern = r'<color=#.{4,12}>.*?</color>'
  #很好，确实可能存在#后面不一定是六位数的情况，优化了 4-12位
  if '<color=#' in detail_desc:   
    #正则啦，思路优化之后是先看看有没有<color=#，有再找
    if not re.search(pattern, detail_desc):
      return False
  return True

def check_total_pp(df, skip_ids):
  try:
    # 创建一个 DataFrame 的副本以避免 SettingWithCopyWarning
    df_filtered = df.iloc[5:].copy()

    # 确保 TotalPP 是数值类型
    df_filtered['TotalPP'] = pd.to_numeric(df_filtered['TotalPP'], errors='coerce').fillna(0)
    zero_pp_indices = df_filtered.index[df_filtered['TotalPP'] == 0].tolist()
    
    issues = [f"行 {index + 6}: 'TotalPP' 字段值为零。" for index in zero_pp_indices if df_filtered.at[index, 'Id'] not in skip_ids]
    return issues
  except Exception as e:
    return [f"check_total_pp 函数错误：{e}"]


# 用于转换可能存在浮点数
def to_str_if_float(value):
  return str(value) if isinstance(value,float) else value

#攻击范围检查
def check_range(df, rules,skip_ids):
  issues = []
  for index, row in df.iterrows():
    if row['Id'] in skip_ids:
       continue
       #这里也得跳
    detail_desc = row['DetailDesc']
    # skill_range = float(row['Range'])
    try:
       skill_range = float(row['Range'])
    except ValueError:
      # 抛就对了
      continue   
    for desc_keyword, expected_range in rules.items():
      if desc_keyword in detail_desc and skill_range != expected_range:
        issues.append(f"行号 {index + 2}, ID={row['Id']}: DetailDesc 包含 '{desc_keyword}'，但 Range 字段的值应为 {expected_range}，当前为 {skill_range}。")
  return issues
#对于属性技能威力的检查
def check_attribute_power(df,rules,skip_ids):
  if df['DetailDesc'].str.contains('攻击').any():
    return []
  #包含攻击则肯定是有威力的，跳出省性能
  issues = []
  for index,row in df.iterrows():
    if row['Id'] in skip_ids:
      continue
    detail_desc = row['DetailDesc']
    try:
        power = float(row['Power'])
    except ValueError:
       continue
    #只能继续抛了
    for desc_keyword,except_power in rules.items():
       if desc_keyword in detail_desc and power !=except_power:
          issues.append(f"行号 {index +2 }, ID = {row['Id']}: DetailDesc包含 '{desc_keyword}',期望 Power 字段的值为 {except_power},当前为 {power}")
  return issues

#技能威力，等级低的不大于高等级的检查
def check_power_consistency(df,skip_ids):
  issues = []
  grouped = df.groupby('Id')
  for skill_id, group in grouped:
    sorted_group = group.sort_values(by='Level')
    prev_power = None
    for index, row in sorted_group.iterrows():
      current_power = row['Power']
      if row['Id'] in skip_ids:
        continue
      if prev_power is not None and current_power < prev_power:
        issues.append(
          f"行号 {index +2 }, 技能ID {skill_id}: 等级 {row['Level']} 的 power ({current_power}) 小于较低等级的 power ({prev_power}).")
      prev_power = current_power

  return issues

#检查priority的一致性
def check_priority(df, issues):
  for id, group in df.groupby('Id'):
    if group['Priority'].nunique() > 1:
      issues.append(f"skill_id= {id}: Priority字段不一致")
#对next_up的检查 
def check_next_up(df, skill_id, level, next_up, index,skip_ids):
  issues = []
  if skill_id in skip_ids:
    return issues
  # 检测 NextUp 字段
  power_match = re.search(r'威力：(\d+)<color=#.{4,10}> ＞ </color><color=#.{4,10}>(\d+)</color>', next_up)
  if power_match:
    current_power = int(power_match.group(1))
    next_power = int(power_match.group(2))
    # 检查当前等级的 Power 值
    if df[(df['ID'] == skill_id) & (df['Level'] == level)]['Power'].iloc[0] != current_power:
      issues.append(f"行 {index}: 当前等级威力值与 'NextUp' 不匹配。")
    # 检查下一等级的 Power 值
    if df[(df['ID'] == skill_id) & (df['Level'] == level + 1)]['Power'].iloc[0] != next_power:
      issues.append(f"行 {index}: 下一等级威力值与 'NextUp' 不匹配。")
  return issues

#塞一起的检查函数
def check_excel(file_path):
  issues = []
  skip_ids = [1123002, 2034001,1084004,100603106,100403104,100007101,1124005,1124003,1124001,1103007,1094007,1104005,1024002,100602104
              ,1014007,1024006,1034001,1044001]  
  # 豁免数组，用于跳过远古遗留   

  try:
    df = pd.read_excel(file_path, engine='openpyxl',header=5)
    df = df.apply(lambda col: col.map(to_str_if_float))  
    #apply 方法将 lambda 函数应用于 DataFrame 的每一列。lambda 函数内部，使用 map 方法对列中的每个元素应用 to_str_if_float 函数
    # print(df.columns)  # 打印列名以进行检查，测试代码
    #存给Range判断用的
    range_rules = {
      "攻击敌方单体": 3,
      "攻击敌方全体": 4,
      "攻击两个相邻的敌方目标": 10,
    }
    #给Power判断用
    power_rules = {
      "提高自身": 0,
      "我方全体": 0,
      "治疗我方单体": 0,
      "提高我方单体": 0,
      "提升我方单体": 0,
      "防御姿态": 0
    }
    #power和range的
    issues.extend(check_power_consistency(df,skip_ids))
    issues.extend(check_range(df, range_rules,skip_ids))
    issues.extend(check_attribute_power(df,power_rules,skip_ids))
    issues.extend(check_total_pp(df, skip_ids))

    for index, row in df.iloc[6:].iterrows():
        #读取各个字段,check_range写的有点问题，所以说先跳过前两行再读表
        skill_id = row['Id']
        detail_desc = row['DetailDesc']
        hit_rate = row['HitRate']
        attack_count = row['AttackCount']
        next_up = row['NextUp']
        level = row['Level']
        power = row['Power']

        if skill_id in skip_ids:
            continue  
      # 检查技能名称中是否包含特殊字符
        if has_special_char(row['Name']):
         issues.append(f"行号{index + 2}: 技能名称包含特殊字符")

      # 检查DetailDesc字段中是否包含“必中”
        if '必中' in detail_desc:
        # 如果同时包含“必中”和“下一回合”，则HitRate可以不为-1
            if '下回合' in detail_desc:
              continue
        # 如果只包含“必中”，则HitRate必须为-1
            elif hit_rate != -1:
              issues.append(f"行号{index + 2}, 技能ID {skill_id}: DetailDesc包含‘必中’，但HitRate不为-1")

      #检查DetailDesc字段的完整性-颜色
        if not check_detail_desc_integrity(row['DetailDesc']):
            issues.append(f"行号{index + 2},ID={skill_id}: DetailDesc字段格式不完整-颜色")
        
    # 新增的检测逻辑
        match = re.search(r'(\d+)段', detail_desc)
        if match:
            if '~' in detail_desc:  #取巧了，这里用的是随机段数里面的 “~” 即随机 3~4段的
              continue
            if '额外攻击' in detail_desc: #同上
              continue
            expected_count = int(match.group(1))
            if expected_count != int(attack_count):
                issues.append(f"行 {index},ID={skill_id}: 'DetailDesc' 中的段数与 'AttackCount' 不匹配。") 
    issues.extend(check_next_up(df,skill_id,level,next_up,index,skip_ids))
    # check_priority(df, issues) 发现貌似会有特殊情况 先注释掉
  except Exception as e:
    issues.append(f"错误：{e}")

  return issues

def main():
  try:
      file_path = "D:pjbn/configs/develop/pm_skill_config#技能.xlsm"
      #存放pem_skill表的路径，这部分是的手动改下的
      result = check_excel(file_path,)
      if result:
         for issue in result:
            print(issue)
      else:
         print("perfect 无错绝地")
  except FileNotFoundError:
      print(f"{file_path}does not exist")
  except pd.errors.ParserError:
     print(f"The file {file_path} is not valid Excel File")

if __name__ == "__main__":
   main()

