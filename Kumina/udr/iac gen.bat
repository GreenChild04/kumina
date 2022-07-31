@echo off
set mypath=%cd%
echo %mypath%
"%mypath%\..\wpis\python.exe" "%mypath%\udrLock\udrLock.py"
PAUSE