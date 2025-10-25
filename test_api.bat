@echo off
chcp 65001 > nul
title JARVIS API Test
color 0E

echo.
echo ========================================
echo         JARVIS API TEST
echo ========================================
echo.

REM Activate virtual environment
call venv_speech\Scripts\activate.bat

echo 🧪 Testing JARVIS API...
python test_api.py

pause