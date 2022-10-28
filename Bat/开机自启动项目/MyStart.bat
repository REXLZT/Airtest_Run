:: 先打开浏览器
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" & ping localhost -n 1
:: 接着打开QQ
start "" "C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe "  & ping localhost -n 1
:: 打开sql
start "" "D:\Program Files (x86)\HeidiSQL\heidisql.exe"  & ping localhost -n 1
:: sourcetree
start "" "C:\Users\linzeteng\AppData\Local\SourceTree\SourceTree.exe"  & ping localhost -n 1
:: Battercallshell
start "" "C:\Users\linzeteng\AppData\Local\Programs\better-call-shell\BetterCallShell.exe"  & ping localhost -n 1
::打开hs，很多都来不及调试
start "" "E:\学习系列\BN\HFS\HFS\HFS\hfs.exe"  & ping localhost -n 1
::打开Typora
start "" "D:\bn_software\typora\Typora.exe"  & ping localhost -n 1
::打开服务器
start "" "C:\Program Files (x86)\Mobatek\MobaXterm\MobaXterm.exe"  & ping localhost -n 1
:: 想了想，再打开个vscode也不错
start "" "C:\Program Files\Microsoft VS Code\Code.exe"  & ping localhost -n 1
:: 补充个foxmail，这玩意也得打开
start "" "C:\Foxmail 7.2\Foxmail.exe"  & ping localhost -n 1
:: 某不知名的软件界面
start "" "D:\bn_software\air\Q-Dir\Q-Dir.exe"  & ping localhost -n 1
:: 录屏也加上
start "" "C:\Program Files (x86)\EVCapture\EVCapture.exe"  & ping localhost -n 1
:: 截图的小玩意
start "" "D:\bn_software\chop\Setuna.exe"  & ping localhost -n 1

taskkill /f /im cmd.exe
exit

