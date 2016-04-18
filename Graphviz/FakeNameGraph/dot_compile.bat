@echo off
set path=%path%;D:\Program Files\Graphviz\2.38\bin;

rem %0   %1     %2      %3
rem self [target type]
echo CurrentBatch:%0
echo Target_File:%1
echo Output:%1.%2
echo AdditionalParaMeter:1:%1 ,2:%2 ,3:%3 ,4:%4, 5:%5 ,6:%6 ,7:%7 ,8:%8 ,9:%9 .



if "%3"=="exit" (
    dot -T%2 %1 -o %1.%2 %4 %5 %6 %7 %8 %9
    exit
    ) else (
    dot -T%2 %1 -o %1.%2 %3 %4 %5 %6 %7 %8 %9
    echo return code:%errorlevel%
    echo ==============Finished.==============
    )