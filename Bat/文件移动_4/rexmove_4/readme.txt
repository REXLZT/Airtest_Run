*这玩意分三步走，第一步就是先把旧文件全部给干掉；

*第二步就是先在指定位置建立好新的文件夹，然后再把新的文件被复制过来；

*第三步就是设置定时任务来执行这个脚本；


----附带个看到的空文件夹删除脚本，可能以后会用得上，但是我这里就直接暴力删除了
@echo off
for /f "delims=" %%a in ('dir /ad /b /s F:\^|sort /r') do (
   rd "%%a">nul 2>nul &&echo 空目录"%%a"成功删除！
)
pause
----------

至于执行的话，为了偷懒我这里就不另外写脚本了，直接调用window的每日定时任务去触发我做的这个rex_move即可
具体的做法如下
cmd里面创建一条命令：
schtasks /create /tn rexmove /tr E:\code\air\demo\Airtest_Run\Bat\rexmove_4\rex_move.bat /sc /DAILY /st 12:00
planB:从控制面板-管理工具-任务计划程序，图形化！