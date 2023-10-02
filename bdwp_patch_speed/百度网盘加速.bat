@REM 中文
chcp 65001
cd PSTools

@REM @echo off
@REM set /p user_input=请输入百度网盘主界面进程PID: 

@REM set /a user_input_as_number=%user_input%
@REM echo 你输入的数字是：%user_input_as_number%

echo 堵塞进程: baidunetdisk.exe
pssuspend baidunetdisk.exe
echo 堵塞进程: yundetectservice.exe
pssuspend yundetectservice.exe
echo 堵塞进程: 百度网盘主界面
@REM pssuspend %user_input_as_number%
pssuspend baidunetdiskhost.exe

@REM 下面是注释内容

@REM echo 下载完成后请按Enter恢复进程


@REM pause
@REM ) else (
@REM     echo 你输入的不是有效的数字。
@REM     pause
@REM )

@REM rem 移除输入中可能包含的引号（如果有的话）
@REM set "user_input=%user_input:"=%"

rem 检查输入是否为数字
@REM setlocal EnableDelayedExpansion
@REM set "is_number=true"
@REM for /L %%i in ("1","2","3","4","5","6","7","8","9","0") do (
@REM     if not "!user_input:%%i=!"=="!user_input!" (
@REM         set "is_number=false"
@REM         goto :break
@REM     )
@REM )
@REM :break
@REM endlocal

@REM rem 如果是数字，将其转换为整数
@REM if "%is_number%"=="true" (