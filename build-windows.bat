@echo off
REM build script for windows distributable

echo ========================================
echo claude workflow setup - windows build
echo ========================================

REM check if python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo error: python not found
    echo install python from https://www.python.org/downloads/
    echo make sure to check "add python to path" during installation
    exit /b 1
)

REM create virtual environment if it doesn't exist
if not exist "venv\" (
    echo creating virtual environment...
    python -m venv venv
)

REM activate virtual environment
echo activating virtual environment...
call venv\Scripts\activate.bat

REM install dependencies
echo installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

REM clean previous builds
echo cleaning previous builds...
if exist "build\" rmdir /s /q build
if exist "dist\" rmdir /s /q dist
if exist "claude-workflow-setup.exe" del /q claude-workflow-setup.exe

REM ensure .claude folder is present
if not exist ".claude\" (
    echo error: .claude folder not found
    echo this script must be run from the project root
    exit /b 1
)

REM build executable
echo building windows executable...
pyinstaller --clean --noconfirm ^
    --onefile ^
    --windowed ^
    --name "claude-workflow-setup" ^
    --hidden-import PySide6.QtCore ^
    --hidden-import PySide6.QtGui ^
    --hidden-import PySide6.QtWidgets ^
    claude_setup.py

REM verify build
if exist "dist\claude-workflow-setup.exe" (
    echo.
    echo ========================================
    echo build successful!
    echo ========================================
    echo.
    echo output: dist\claude-workflow-setup.exe
    echo.
    echo to test:
    echo   dist\claude-workflow-setup.exe
    echo.
    echo to distribute:
    echo   1. zip the dist folder or just the .exe file
    echo   2. share the .zip file
    echo.
    echo note: windows may show a smartscreen warning for unsigned apps
    echo       click "more info" then "run anyway"
    echo.
) else (
    echo.
    echo ========================================
    echo build failed!
    echo ========================================
    echo check the output above for errors
    exit /b 1
)
