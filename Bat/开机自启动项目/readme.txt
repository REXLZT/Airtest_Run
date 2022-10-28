1. ::这个在bat批处理中是行注释

2. @echo off是执行批处理的命令的意思

3.ping localhost -n 2可以当做是定时器，2 是两秒的意思。如果修改延时或者去掉，改& ping localhost -n 2即可

4.最后两行的意思是执行完命令后关闭cmd命令窗口

5.关键一步，把这个塞到开机启动项里面即可------  路径是酱紫的（我错大发了）： C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp