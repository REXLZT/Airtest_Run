# -*- encoding=utf8 -*-
__author__ = "linzeteng"

from airtest.core.api import *
from airtest.core.android.android import ADB, Minitouch

import warnings
warnings.simplefilter("always")

auto_setup(__file__)

#备注：基于k50G写的，mobileType=k50G
mobileType ='k50G'
# 修改全局设置threshold
ST.THRESHOLD = 0.8
#初始化一下，存放用于防止走歪导致卡死

def tryTouch(img):
    try:
        touch(wait(img,timeout=1))
        # 用来尝试点击，没有就退出
    except:
        pass
    
def swipe2Right(startPosition):
    swipe(startPosition, vector=[-0.45,0])

def test_swipe(self):
        for i in (TOUCH_METHOD.ADBTOUCH, TOUCH_METHOD.MINITOUCH, TOUCH_METHOD.MAXTOUCH):
            self.android.touch_method = i
            self.android.swipe((100, 100), (300, 300))
            self.android.swipe((100, 100), (300, 300), fingers=1)
            self.android.swipe((100, 100), (300, 300), fingers=2)        
        self.android.touch_method = TOUCH_METHOD.ADBTOUCH
        self.android.swipe((100, 100), (300, 300), fingers=3)
        self.android.touch_method = TOUCH_METHOD.MINITOUCH
        with self.assertRaises(Exception):
            self.android.swipe((100, 100), (300, 300), fingers=3)
            
def _count_server_proc(self):
        output = self.adb.raw_shell("ps").strip()
        cnt = 0
        for line in output.splitlines():
            if "minitouch" in line and line.split(" ")[-2] not in ["Z", "T", "X"]:
                # 进程状态是睡眠或运行---用于在新手的时候等待开场动画
                cnt += 1
        return cnt
      
def touch3pic(List):
    #优化下图像识别，这样子在三张图片中找到如何就执行
    picList = [pic1,pic2,pic3]
    for pic in picList:
        pos=exists(pic)
        if pos:
            touch(pos)
            break
            
            
            
#游戏开场动画的等待判定（通过是否有载具模块来判定）
# if a = exists(Template(r"tpl1665480442248.png", record_pos=(-0.377, -0.156), resolution=(2400, 1080)))
#     touch(a)
#     elif sleep(50) break
# assert_exists(Template(r"Template(r"tpl1665480442248.png", record_pos=(-0.377, -0.156), resolution=(2400, 1080))"),"over")
#操控滑杆进行瞎移动
swipe((355,855),vector=[-0.0008,-0.2412],duration=10)
#地图跳转
touch((300,260),duration=0.5,times=3) #地图按钮
sleep(0.5)
touch((2143,1028),times=3)
sleep(1)
touch((2108,357),times=3)#思伍德区
sleep(1)
touch((1417,980),times=1)#出生地
touch((2060,995),times=1)#传送按钮
swipe((355,855),vector=[-0.0008,-0.2412],duration=100)
keyevent("BACK") 
touch((1095,682),times=1)