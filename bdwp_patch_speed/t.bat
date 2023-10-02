@REM 中文
chcp 65001

@echo off

cd TCPView


@echo off
setlocal enabledelayedexpansion

REM 执行命令并将结果保存到变量
for /f "delims=" %%a in ('tcpvcon -a -c -n 18008') do set "result=%%a"

REM 显示结果
echo Result: %result%




endlocal


@REM @REM tcpvcon [-a] [-c] [-n] [process name or PID]


@REM @echo off
@REM setlocal enabledelayedexpansion

@REM REM 执行命令并将输出存储在变量中
@REM for /f "delims=" %%i in ("tcpvcon -a -c -n 18008") do (
@REM     set "output=!output! %%i"
@REM )

@REM REM 显示存储的输出
@REM echo "%output%"

@REM endlocal
