REM File to unpack data is the correct password is given.

@echo off

set key=*****

title ::
color 0a
echo Please enter your password:
set/p "pass= >"
if %pass%==%key% goto UnPack
cls
color 0c
echo That is not the password! Aborting unpack!
echo.
pause
exit
:UnPack
set dest=C:\Contents.txt
cls
echo That is the correct passord!
echo.
echo Your data will unpacked and sent here: %dest%
echo.
echo Please make sure this file does not already exist before continuing
echo as this may ruin your data.
echo.
pause
cls

echo $$$$$>>%dest%

echo Unpack complete!
echo.
echo Your data can be found here: %dest%
echo.
pause
exit