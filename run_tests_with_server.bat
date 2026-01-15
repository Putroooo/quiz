@echo off
echo ========================================
echo Starting PHP Server and Running Tests
echo ========================================

:: Start PHP server in background
echo Starting PHP server on port 8000...
start /B cmd /c "C:\xampp\php\php.exe -S localhost:8000"

:: Wait for server to start
timeout /t 5 /nobreak

:: Run tests
echo.
echo Running tests...
cd tests
py run_all_tests_with_screenshots.py

:: Stop PHP server
echo.
echo Stopping PHP server...
taskkill /F /IM php.exe 2>nul

echo.
echo Done!
pause
