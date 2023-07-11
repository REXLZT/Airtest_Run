def process_strings(strings):
    result = []
    
    for string in strings:
        
        # 识别 Services 并删除其前面的内容
        index = string.find('Services')
        if index != -1:
            string = string[index:]
        # 删除结尾的 .lua
        string = string.replace('.lua', '')
        # 将 / 转换成 .（踩坑了 试了半天才想起来，用破树复制的路径直接就是文件路径了，window的路径是反斜杠
        string = string.replace( '\\', '.').replace('/','.')
        # 强化一波，加上了直接用命令获取当前哈希值对应提交的文件路径
        #  命令是： git diff-tree --no-commit-id --name-only -r 6bd0ec3ca5be6da1a0cdec4c70e160835fa94ad3 （结尾加的是40位的哈希值）
        result.append(string)

    return result

if __name__ == "__main__":
    input_strings = input("请输入多个字符串，用空格间隔：").split()
    processed_strings = process_strings(input_strings)
    print("处理后的字符串列表：")
    for s in processed_strings:
        print(s)
def process_strings(strings):
    result = []
    
    for string in strings:
        index = string.find('Services')
        if index != -1:
            string = string[index:]
        string = string.replace('.lua', '')
        string = string.replace('\\', '.').replace('/', '.')
        result.append(string)

    return result

# if __name__ == "__main__":
#     print("请输入多个字符串，用空格或换行间隔：")
#     input_text = input().replace('\n', ' ')
#     input_strings = input_text.split()
#     processed_strings = process_strings(input_strings)
#     print("处理后的字符串列表：")
#     for s in processed_strings:
#         print(s)




