@echo off
setlocal
pushd "%~dp0"

dir /b *.c > sources.txt
findstr /r "." sources.txt >nul
if errorlevel 1 (
  echo No C source files found in this folder.
  del sources.txt
  popd
  exit /b 1
)

gcc -std=c11 -Wall -Wextra -O2 @sources.txt -o app.exe
if errorlevel 1 (
  echo Build failed.
  del sources.txt
  popd
  exit /b 1
)

del sources.txt
echo Build successful: app.exe

popd
endlocal