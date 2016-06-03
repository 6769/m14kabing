# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image,ImageChops
import os
import logging
import sys

pause_mark=False
mark_of_new='.Inverted.'
help_string="""

PIL invert 0.2 简单的反色工具
用法： 应用程序.exe  File...
       或者直接将图片拖曳到exe图标上
举例： BatchImageToreverseColor.exe testpic0.png testpic1.png testpic2.png...


"""

logging.basicConfig(level=logging.INFO)
def picReverse(addr):
    logging.info('[%s]start To solve'%addr)
    try:
        currntpic=Image.open(addr)
    except OSError as e:
        print(e)
        logging.info(e)
        logging.info('------------Failed,file didn\'t open----------')
        pause_mark=True
        return e
    picformat=currntpic.format
    newpic=ImageChops.invert(currntpic)
    
    newfilename=addr+mark_of_new+picformat.lower()
    logging.info('[%s]start To save the inverted pic'%newfilename)
    try:
        newpic.save(newfilename)
        logging.info('------------Success,file saved------------')
    except :
        logging.info('[%s] save Error'%newfilename)
        logging.info('********Please give Author a feedback********')
        pause_mark=True
    
def main(argv=None):
    if(argv==None):
        piclist=sys.argv[1:]
    else:
        piclist=argv
        
        
    if(piclist==[]):
        logging.info(help_string)
        os.system('pause')
        sys.exit(0)
        
    for i in piclist:
        picReverse(i)
    if(pause_mark):
        os.system('pause')
        
        
if __name__=='__main__':
    debug=0
    if(debug==1):
        main(['testpic.png',])
    else:
        main()

    