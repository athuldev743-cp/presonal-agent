@echo off
chcp 65001 > nul
title JARVIS Voice Mode
color 0B

echo.
echo ========================================
echo       JARVIS VOICE ASSISTANT
echo ========================================
echo.

REM Activate virtual environment
call venv_speech\Scripts\activate.bat

echo 🎤 Starting JARVIS Voice Mode...
echo 🗣️  Speak your commands after the beep
echo ⏹️  Say "exit", "quit", or "bye" to stop
echo.

REM Start voice mode
python main.py

pause