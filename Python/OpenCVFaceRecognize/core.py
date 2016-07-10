# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 22:41:32 2016

@target: class implemented application by commandline.

@reference:thanks to whom build these pages
http://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_api.html#createlbphfacerecognizer
https://en.wikipedia.org/wiki/Local_binary_patterns


@author: pip
"""

import cv2
#import threading
#import time
import logging
import numpy as np
#import os
#import sys
logging.basicConfig(level=logging.DEBUG)

from cameraIO import IOSteam
from faceDetect.trackers import FaceTracker
#from faceRecognize.facepp import API,File
#from faceRecognize.apikey import API_KEY, API_SECRET
#api = API(API_KEY, API_SECRET)

class core(object):
    Available_Mode=['train','recognize']
    Uniform_Size=(40,40)
    def __init__(self,useGUI=False,debugWin=True,
                 drawFaceRct=True,
                 faceRecognize=True,faceRecognizeXmlfile=None):
        self._useGUI=useGUI
        self._debugWin=debugWin
        self.drawFaceRct=drawFaceRct
        #self.drawMoveRct=drawMoveRct
        self.faceRecongnize=faceRecognize
        self._recognizeFace_xml_file=faceRecognizeXmlfile

        self._front=IOSteam()
        self._detectFace=FaceTracker()
        self._recognizeFace=cv2.createLBPHFaceRecognizer(neighbors=8)
        self.displayFrame=None
        try:
            self._recognizeFace.load(self._recognizeFace_xml_file)

        except:
            logging.debug('[-]recognize DB xml file:{} fail to load'.format(
                                                self._recognizeFace_xml_file))
            logging.info( '[-]without DB xml ,recognize may be reported Error!')
        #self._trackers=[]
        self._faceLost=False
        #self._faceReg_api=API(API_KEY, API_SECRET)
        self._res=[]
        self._mode=self.Available_Mode[0]
        
        
        self.faceSetinSameFrame=[]
        self.faceSetofImageinSameFrame=[]
        self.faceSetofImageinSameFrameResized=[]
        
        
    def _resize_to_Uniform_Size(self,frame):
        return cv2.resize(frame,self.Uniform_Size)

    def _face_detection(self,frame):
        #backup display
        #self._res=[]
        self.displayFrame=frame.copy()
        
        
        self._detectFace.update(frame)
        faces=self._detectFace.faces
        self.faceSetinSameFrame=[face.faceRect for face in faces]
        
        if(self.faceSetinSameFrame!=[]):
            logging.info('faceSetinSameFrame :{}'.format(self.faceSetinSameFrame))
            self.faceSetofImageinSameFrame=[i.faceImage for i in faces]
            self.faceSetofImageinSameFrameResized=list(map( self._resize_to_Uniform_Size,
                                                    self.faceSetofImageinSameFrame ))
        if(self.drawFaceRct):
            self._detectFace.drawDebugRects(self.displayFrame)
    
    
    def _main_recognize_once(self,frame):
        self._face_detection(frame)
        #if self._faceLost:
#        self._detectFace.update(frame)
#        faces=self._detectFace.faces
#        self.faceSetinSameFrame=[face.faceRect for face in faces]
#        if(self.faceSetinSameFrame!=[]):
#            self.faceSetofImageinSameFrame=[i.faceImage for i in faces]
#            self.faceSetofImageinSameFrameResized=list(map( self._resize_to_Uniform_Size,
#                                                    self.faceSetofImageinSameFrame )
#                                                    )
        if(self.faceSetinSameFrame!=[]):
            #recognize mode
            res=[]
            self._res=[]
            for i in self.faceSetofImageinSameFrameResized:
                res.append(self._recognizeFace.predict(i))

            #load result  (Rectzone,(may be the person,confidence))
            for facezone,whomheis in zip(self.faceSetinSameFrame,res ):
                self._res.append(dict(zone=facezone,who=whomheis ))
            logging.info('FaceRecognize result: {}'.format(self._res))
            #result has been saved.
            
        #else:
            #logging.info('Noface found')
            
    def _main_train_once(self,frame,label):
        """
        only accept One integer label to train.
        """
        if(type(label)!=int):
            raise TypeError('label {} must be an integer'.format(label))

        self._face_detection(frame)


#        self._detectFace.update(frame)
#        faces=self._detectFace.faces
#        faceSetinSameFrame=[face.faceRect for face in faces]
        if(self.faceSetinSameFrame!=[]):
#            faceSetofImageinSameFrame=[i.faceImage for i in faces]
#            faceSetofImageinSameFrameResized=list(map( self._resize_to_Uniform_Size,
#                                                    faceSetofImageinSameFrame )
#                                                    )
            xlabel=np.asarray([label,], dtype=np.int32)
            
            self._recognizeFace.update([self.faceSetofImageinSameFrameResized[0],],xlabel)
            
            logging.info('faceUpdated {}'.format(xlabel))

    def train(self,frame,label):
        self._main_train_once(frame,label)
        
    def saveTrainSet(self,filename=None):
        if filename!=None:
            _filename=filename
        else:
            _filename=self._recognizeFace_xml_file
        if _filename!=None:
            self._recognizeFace.save(_filename)
        else:
            logging.debug('No file Name for _recognizeFace_xml_file!')
    def recognize(self,frame):
        self._main_recognize_once(frame)
        
    @property
    def result(self):
        return self._res
        
if __name__=='__main__':
    print('In main logic')













