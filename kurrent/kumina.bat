@echo off
set mypath=%cd%
echo %mypath%
"%mypath%/../Kumina/wpis/python.exe" "%mypath%/../Kumina/shell.py" %1
PAUSE