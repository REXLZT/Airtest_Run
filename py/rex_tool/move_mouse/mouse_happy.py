import pyautogui as gui
import random as r

gui.FAILSAFE =True
a=0
print("嘎嘎嘎你的鼠标被我操控了")
while a<=10:
    gui.moveTo(r.randint(1,1919),r.randint(1,1079)) 
# a+=1