# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 19:09:34 2016

@author: pip
"""

import cv2
import threading
import time
import os
from pylab import *
import random
from collections import deque

import logging
logging.basicConfig(level=logging.DEBUG)

filelist=[i for i in os.listdir('.') if i.endswith('png')]
logging.info(time.ctime())
wnm='2'
cv2.namedWindow(wnm)
filelist_img=map(cv2.imread,filelist)
#for i in filelist_img:
#    #frame=cv2.imread(i)
#    #cv2.imshow('2',frame)
#    cv2.imshow('2',i)
#    time.sleep(1)
while cv2.waitKey(1) == -1:
    cv2.imshow(wnm,random.choice(filelist_img))
    #time.sleep(0.5)
    #break