@echo off
echo =======================================
echo   Quantum Go - ZidanAI Setup
echo =======================================
echo.

echo [1/3] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found! Please install Python 3.8 or higher.
    pause
    exit /b 1
)
echo.

echo [2/3] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)
echo.

echo [3/3] Starting Flask application...
echo.
echo =======================================
echo   Server will start at:
echo   http://localhost:5000
echo =======================================
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
