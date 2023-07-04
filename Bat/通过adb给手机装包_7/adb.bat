@echo off
setlocal enabledelayedexpansion

set ADB_PATH=C:\Users\YourUserName\AppData\Local\Android\Sdk\platform-tools\adb.exe  # adb 工具路径
set APK_DIR=D:\adb-install  # APK 文件所在目录

echo Searching for APK files...
for %%a in ("%APK_DIR%\*.apk") do (
    echo Installing "%%~nxa"...
    "%ADB_PATH%" devices | findstr /e "device" >nul
    if %errorlevel% == 0 (
        echo Device found.
        "%ADB_PATH%" -r install "%%~fa"
        echo Done.
    ) else (
        echo No device found.
    )
    pause
)

pause
