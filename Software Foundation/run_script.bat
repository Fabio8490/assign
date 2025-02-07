@echo off
REM Script to execute the data processing program  For Windows

if "%~1"=="" (
    echo Usage: run_script.bat ^<input_file^>
    exit /b 1
)

python data_processor.py %1

