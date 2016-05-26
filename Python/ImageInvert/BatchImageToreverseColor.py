# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image,ImageChops
import os
import logging
import sys
mark_of_new='.Inverted.'
logging.basicConfig(level=logging.INFO)
def picReverse(addr):
    logging.info('[%s]start To solve'%addr)
    try:
        currntpic=Image.open(addr)
    except OSError as e:
        print(e)
        logging.info(e)
        return e
    picformat=currntpic.format
    newpic=ImageChops.invert(currntpic)
    
    newfilename=addr+mark_of_new+picformat.lower()
    logging.info('[%s]start To save the inverted pic'%newfilename)
    try:
        newpic.save(newfilename)
        
    except :
        logging.info('[%s] save Error'%newfilename)
        logging.info('********Please give Author a feedback********')
    logging.info('------------Success,file saved------------')
def main(argv=None):
    if(argv==None):
        piclist=sys.argv[1:]
    else:
        piclist=argv
    for i in piclist:
        picReverse(i)
        
        
if __name__=='__main__':
    debug=0
    if(debug==1):
        main(['testpic.png',])
    else:
        main()
    
    
    
    
    