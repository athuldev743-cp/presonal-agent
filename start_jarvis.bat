@echo off
chcp 65001 > nul
title JARVIS AI Assistant
color 0A

echo.
echo ========================================
echo         JARVIS AI ASSISTANT
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv_speech\Scripts\activate.bat" (
    echo ❌ Virtual environment not found!
    echo Please make sure you're in the correct directory.
    pause
    exit /b 1
)

REM Activate virtual environment
echo 🔧 Activating Python environment...
call venv_speech\Scripts\activate.bat

REM Check if .env file exists
if not exist ".env" (
    echo ⚠️  Warning: .env file not found!
    echo Make sure you have OPENAI_API_KEY in .env file
    echo.
)

REM Install/update required packages
echo 📦 Checking/installing required packages...
pip install fastapi uvicorn openai requests beautifulsoup4 python-dotenv wikipedia speechrecognition pyttsx3 torch torchaudio speechbrain --quiet

echo.
echo 🚀 Starting JARVIS API Server...
echo.
echo 📡 Server will be available at: http://127.0.0.1:8000
echo 📚 API Docs:          http://127.0.0.1:8000/docs
echo 🎤 Voice Mode:        Run 'python main.py' in another terminal
echo 🌐 Frontend:          https://personal-ai-front.vercel.app
echo.
echo ⏹️  Press Ctrl+C to stop the server
echo ========================================
echo.

REM Start the FastAPI server
uvicorn main_api:app --reload --port 8000

pause