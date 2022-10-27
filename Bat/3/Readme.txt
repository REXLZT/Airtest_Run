这个嘞，也没啥，就是为了统一下安装效率而写的脚本，按一下一键安装貌似会快捷蛮多的

具体的都写在安装运行环境这个bat里面，实现原理也是蛮简单的，就是通过pip来实现，关联到的就是requirements.txt这个文件
@echo off
start cmd /K  "pip install -r requirements.txt"

