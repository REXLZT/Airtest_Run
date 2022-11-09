@echo off
rd /s /q E:\code\Miscellaneous_Studies\All_in_study\
:: 总之先删除，防止冲突
@echo off
xcopy E:\All_in_study\ E:\code\Miscellaneous_Studies\All_in_study\ /s /y /h /r /q
:: 然后再all in的复制过去，有什么改什么就是了