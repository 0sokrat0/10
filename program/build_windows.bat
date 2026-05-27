@echo off
echo Установка PyInstaller...
pip install pyinstaller

echo Сборка EXE...
pyinstaller --onefile --windowed --name "ReactorMonitor" --add-data "help;help" main.py

echo.
echo Готово! Файл: dist\ReactorMonitor.exe
pause
