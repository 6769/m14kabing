color 03
rem 指定控制台输出的颜色属性
@echo off
cls

echo Environments Require:
echo Python 2.7.11,numpy,cv2,PIL,scipy
echo -----------------------------------------------------
echo Python version:
python -V
echo Library check :
python -c "import time;print(time.ctime())"
python -c "import cv2 ;print('openCV confirmed\n')"
echo -----------------------------------------------------
echo Usage:
type readme.txt
echo .
echo =====================================================
echo ================= Press Any Key to Run ==============
echo =====================================================
pause

ipython app.py
echo =====================================================
pause