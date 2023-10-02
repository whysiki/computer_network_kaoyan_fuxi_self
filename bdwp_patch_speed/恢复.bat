@REM 中文
chcp 65001
cd PSTools

@echo off


echo 恢复进程: baidunetdisk.exe
pssuspend baidunetdisk.exe -r
echo 恢复进程: yundetectservice.exe
pssuspend yundetectservice.exe -r 
echo 恢复进程: 百度网盘主界面
pssuspend baidunetdiskhost.exe -r


@REM echo 终止百度网盘
@REM TASKKILL /F /IM baidunetdisk.exe /IM yundetectservice.exe /IM baidunetdiskhost.exe  /T