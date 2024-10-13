@echo off


python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)


IF EXIST requirements.txt (
    echo Installing required Python libraries...
    pip install -r requirements.txt
) ELSE (
    echo requirements.txt not found. Installing default requirements...
    pip install requests
)


echo Running the Python script...
python main.py

pause
