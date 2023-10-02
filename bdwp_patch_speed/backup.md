@REM 参数	说明
@REM -a	显示所有终结点（默认为显示已建立的 TCP 连接）。
@REM -c	将输出打印为 CSV。
@REM -n	不要解析地址。



@REM @REM tasklist /FI "PID eq 10808"
@REM @echo off
@REM set "PID_TO_CHECK=14652"  
@REM @REM set "PID_TO_CHECK=18008"  
@REM REM 将此处的 1234 替换为要检查的进程PID

@REM tasklist /FI "PID eq %PID_TO_CHECK%" 2>nul | find /i "%PID_TO_CHECK%" >nul
@REM if %errorlevel% equ 0 (
@REM     echo 进程 %PID_TO_CHECK% 是一个后台进程。
@REM ) else (
@REM     echo 进程 %PID_TO_CHECK% 不是后台进程，或者不存在。
@REM )




@REM set "pa=18008"  
@REM REM 替换为你的第一个进程的 PID

@REM REM 获取第一个进程的网络使用量
@REM for /f "usebackq tokens=2" %%a in (`tasklist /nh /fi "pid eq %pa%" ^| find /i "%pa%"`) do set "network_usage_1=%%a"

@REM REM 显示网络使用量
@REM echo 进程 %pa% 的网络使用量: %network_usage_1%

@REM pause