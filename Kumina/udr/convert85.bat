@echo off
set py="../wpis/python.exe"
set convScript="utils/convScript.py"
echo Welcome to the base85 converter!
echo:
set /p script="Enter Your Script: "
%py% %convScript% -t %script%
PAUSE                 