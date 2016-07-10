# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:50:56 2016

@author: pip
"""


import cv2
import time
import logging
import os
from window.previewWindowManager import PreviewWindowManager
from core import  core
from cameraIO import  IOSteam

logging.basicConfig(level=logging.DEBUG)
from namelist import name_infaceDB


#name_infaceDB=['pip','sun','Spring','long','King','Miss']
#               0,    1     2       3       4

#faceIDmatchName=dict()

id=list(range(len(name_infaceDB )))
faceIDmatchName=dict(zip(id,name_infaceDB))
def draw_name(img,namestr,pos):
        #draw name near the people
    font = cv2.FONT_HERSHEY_SIMPLEX
    color=(0,255,0)
    cv2.putText(img,namestr,pos, font, 1,color)
     


class application(object):
    def __init__(self,xmlfile='./train/mytrainSet.xml',imgDB='faceDB'):

        self._xmlfile=xmlfile

        self._trainedImgPostion=imgDB
        self._imgMat=[]
        self._label=[]

        self._core=core(faceRecognizeXmlfile=self._xmlfile)
        self._iosteam=IOSteam()
        self._window=PreviewWindowManager('TrainWindows',self.onKeypress)
        self._window_faceZone=PreviewWindowManager('TrainWindows.FaceZone')

        self._trained_file_used=False
        self._keep_run=True
        self._apply_recognize=False

        self.train_setted_img()
    def _link_img_lable(self,img,label):
        self._imgMat.append(img)
        self._label.append(label)

    
        
    def _load_image_trained(self):
        oswalk=list(os.walk(self._trainedImgPostion))
        for current_dir,sub_dir,sub_file in oswalk:
            if sub_file!=[]:
                for eachfile in sub_file:
                    fileposition=current_dir+'\\'+eachfile
                    img=cv2.imread(fileposition)
                    label=current_dir.split('\\')[-1]
                    self._link_img_lable(img,int(label))
                    
                    logging.debug('file walker:filePosition:{}  label:{}'.format(
                                                                fileposition, label  ))
                    
                    
    def onKeypress(self, keycode):
        """Handle a keypress.

        space  -> Take a screenshot.
        escape -> Quit.
        r      -> Reverse mode of faceRecognize,(default:off)
        m      -> Move png file to faceSetDataBase,Please input an integer[1,2,3,4,5...] to tell the programe how to settle current *.png.after operation,png files will be moved to (./faceDB/[label]/i.png)
        """
        if keycode == 32: # space
            self._iosteam.dumpFrame()

        elif keycode == 27: # escape
            #self._windowManager.destroyWindow()
            self._keep_run=False
        elif keycode == ord('r'):
            #activate face recognize
            self._apply_recognize=not self._apply_recognize
            logging.info('[+]app recognize mode change to {}'.format(
                                                        self._apply_recognize))
                                                        
                                                        
            if self._apply_recognize:
                #self.train_setted_img()
                pass
            
        elif keycode == ord('m'):
            #move file .png to label
            label=raw_input('[*]Please input the interger ID of current dirs\' photo:\n')
            try:
                os.mkdir('./faceDB/'+label)
            except WindowsError as e:
                logging.info('Directory error{},means that existed'.format(e))
            filename=[i for i in os.listdir('.') if i.endswith('png')]
            logging.info('file:{}'.format(filename))
            if 0==os.system('mv *.png ./faceDB/'+label):
                logging.info('[+]*.png moved Successfully')
            else:
                logging.info('[-]*.png moved Fail')

            
    def train_setted_img(self):
        """
        run during the init of app,pre train gived image with label
        """
        self._load_image_trained()
        for i in range(len(self._label)):
            self._core.train( self._imgMat[i],self._label[i] )
            logging.debug('pre train step used img{} ,label{} '.format(
                                            self._imgMat[i].shape,self._label[i]))
        self._trained_file_used=True
        
    def _runwithIOSteam(self):
        self._window.createWindow()
        self._window_faceZone.createWindow()
        self._iosteam.run()
        while self._keep_run:
            
            frame=self._iosteam.frame
            if(frame==None):
                continue
            #face recognize
            if self._apply_recognize:
                self._core.recognize(frame)
                result=self._core.result
            else:
                #just detect faceZone
                self._core._face_detection(frame)
            #preview result here
            whattoShow=self._core.displayFrame
            if self._apply_recognize:
                self._draw_name_in_frame(whattoShow)
            
            self._window.show(whattoShow)
            if self._core.faceSetofImageinSameFrameResized!=[]:
                self._window_faceZone.show(self._core.faceSetofImageinSameFrameResized[0])
            self._window.processEvents()

        self._iosteam.stop()
        self._window.destroyWindow()
        self._window_faceZone.destroyWindow()
    def _draw_name_in_frame(self,frame):
        for eachPeople in self._core.result:
            true_name=faceIDmatchName[eachPeople['who'][0]]
            dist=str(eachPeople['who'][1])
            pos=tuple(eachPeople['zone'][:2])
            draw_name(frame,true_name+dist,pos)
            
    def run(self):
        if(self._trained_file_used):
            self._runwithIOSteam()
        else:
            logging.debug('faceDB do not used in Train')




if __name__=='__main__':
    app=application(xmlfile=None)
    app.run()




