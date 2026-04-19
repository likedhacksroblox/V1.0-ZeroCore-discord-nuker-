@echo off
chcp 65001 >nul
title ZeroCore - Installer

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║               ZeroCore Server Fucker Installer             ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

echo [1/3] Updating pip...
python -m pip install --upgrade pip --user

echo.
echo [2/3] Installing discord.py...
python -m pip install discord.py==2.4.0 --user --force-reinstall

echo.
echo [3/3] Installation finished.
echo.
echo Now you can run ZeroCore with Run.bat
echo.

pause