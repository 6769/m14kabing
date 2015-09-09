# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:04:29 2015

@author: pip

@email:5pipitk@gmail.com
"""
import os, sys
maxsize=50

def getdirsize(dire):
    size = 0
    for root, dirs, files in os.walk(dire):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size
    #byte as weight

def mainclean(yourdir=sys.argv[1]):
    target=yourdir
    fileanddir = os.listdir(target)
    for i in fileanddir:
        rawpath=os.path.join(target,i)
        if os.path.isfile(rawpath):
            size=os.path.getsize(rawpath)
            if size>maxsize*1024**2:
                try:                
                    os.remove(rawpath)
                except:
                    pass
    
if __name__=='__main__':
    mainclean()