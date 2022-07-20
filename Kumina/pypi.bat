@echo off
set /p mod="Enter module: "
set space=LOG:
echo Installing: %mod%
echo %space%
"%cd%/wpis/python.exe" -m pip install %mod%
PAUSE