# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:52:54 2016

@author: pip
"""

import cv2
import time
import logging
from window.previewWindowManager import PreviewWindowManager
from core import  core
from cameraIO import  IOSteam

logging.basicConfig(level=logging.DEBUG)

class trainLimitFrame(object):
    def __init__(self,framelength=100,label=0,xmlfile='./train/mytrainSet.xml'):
        self._framelen=framelength
        self._xmlfile=xmlfile
        self._label=label
        self._core=core(faceRecognizeXmlfile=self._xmlfile)
        self._iosteam=IOSteam()
        self._window=PreviewWindowManager('TrainWindows')
        self._window_faceZone=PreviewWindowManager('TrainWindows.FaceZone')
    def run(self):
        self._window.createWindow()
        self._window_faceZone.createWindow()
        self._iosteam.run()
        for i in range(self._framelen):
            logging.info('current frame: {}'.format(i))
            frame=self._iosteam.frame
            
            
            
            self._core.train(frame,self._label)
#            self._core._face_detection(frame)
            
            whattoShow=self._core.displayFrame
            self._window.show(whattoShow)
            if self._core.faceSetofImageinSameFrameResized!=[]:
                self._window_faceZone.show(self._core.faceSetofImageinSameFrameResized[0])
            cv2.waitKey(1)
        self._iosteam.stop()
        self._core.saveTrainSet()
        self._window.destroyWindow()
        self._window_faceZone.destroyWindow()
            
if __name__=='__main__':
    train=trainLimitFrame(10,1)
    train.run()
    
    
    
    