@echo off
REM Activate the Anaconda environment
call C:\Path\To\Anaconda\Scripts\activate.bat <markerless tracking env>
REM Run your Python script in a new minimized window
start /b python C:\Path\To\Current\Directory\MT_GUI.py
