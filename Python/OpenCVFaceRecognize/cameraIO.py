# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:20:57 2016
@usage : Camera Steam I/O Class,use deque and multithreading to increase fetch.
         Frame Storage in limited length container.


@author: pip
"""
import cv2
import threading
import time
from pylab import *
import random
import os
from collections import deque
from window.previewWindowManager import PreviewWindowManager
import logging
logging.basicConfig(level=logging.DEBUG)

class IOSteam(object):
    """
    Implements of frame fetch.    
    """
    def __init__(self,channel=0,queue_len=30,subthreadName='cameraIO'):
        self._subthreadName=subthreadName        
        self._channel=channel
        self._queue_len=queue_len
        self._cameraCapture=cv2.VideoCapture(self._channel)
        self._threading_obj=threading.Thread(target=self._update_frame_continues
                                        ,name=self._subthreadName#,args=(self)
                                        )
        #self._latest_frame_signal=threading.Semaphore(n=0)
        self._latest_frame_signal=threading.Event()
        #last frame
        self._frame=None
        self._frame_count=0
        self._dumped_Frame_count=0
        self._jump_init_camera_frame=10
        self._keep_fetch=False
        self._rate=0
        self.framequeue=deque([],self._queue_len)
        
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None
    @property
    def frame(self):
        # if(len(self.framequeue)>0):
            # #return last appended frame data
            # return self.framequeue[-1]
        # else:
            # return None
        if self._keep_fetch==False or self._threading_obj.isAlive()==False:
            logging.debug('[-]before Fetch frame,use run() method')            
            return None
        else:
            self._latest_frame_signal.wait()
            self._latest_frame_signal.clear()#reset signal until another threading SET.
        #wait for  synchronous signal arrived.
            return self._frame
    @property        
    def rate(self):
        return self._rate
    def _update_frame(self):
        """
        update 1 frame in one manipultion.
        """
        flag=self._cameraCapture.grab()
        if flag:
            
            _,self._frame=self._cameraCapture.retrieve()
            #increase signal count;
            self._frame_count+=1
            if self._frame_count>self._jump_init_camera_frame:
                self._latest_frame_signal.set()
                self.framequeue.append(self._frame)
    def _update_frame_continues(self):
        while self._keep_fetch:
            self._update_frame()
            
            
    def dumpFrame(self,direct='./',filename=None  ,ext='.png'):
        randomstr=str(random.random())[2:7]
        sp='_'
        if filename is None:
            filename=str(int(  time.time()  ))

        dir_filename=direct+filename+sp+str(self._dumped_Frame_count)+sp+randomstr+ext
        if self._keep_fetch and self._threading_obj.isAlive():
            safeFrame=self.framequeue[-1]
            
            if cv2.imwrite(dir_filename,safeFrame):
                self._dumped_Frame_count+=1
                logging.debug('[+]DumpFrame Fetched and Saved {}'.format(filename))
            else:
                logging.debug('[-]DumpFrame Fetched but Not Saved')
        else:
            logging.debug('[-]threading Not running,No dump')
            
            
            
    def control_thread_obj(self,keepRun=True):
        #pass
        if keepRun:
            #consult threading is running?
            if not self._threading_obj.isAlive():
                self._keep_fetch=True
                self._threading_obj.start()
                logging.info('threading keep fetch RUN')
            else:
                logging.info('threading already in RUN')
        else:
            if self._threading_obj.isAlive():
                #self._threading_obj.start()
                self._keep_fetch=False
                logging.info('threading keep fetch will stop')
                time.sleep(0.5)
                logging.debug('interal Thread obj status :%s'%str(
                                                self._threading_obj.isAlive() ))
    def closecamera(self):
        self._cameraCapture.release()
        logging.info('Channel %d released'%self._channel)
        #up to now ,dont now how to do.
    def run(self):
        #self._cameraCapture=cv2.VideoCapture(self._channel)
        self.control_thread_obj(True)
    def stop(self):
        self.control_thread_obj(False)
        self.closecamera()
        
        

def main():
    testWin=PreviewWindowManager('debug')
    testWin.createWindow()
    front=IOSteam()
    n=10
    front.run()
    #cv2.namedWindow('DebugWindow0')
    
    for i in range(n):
        #front._update_frame()
        try:
            lastFrame=front.frame
            #lastFrame=front.framequeue[-1]
            testWin.show(lastFrame)
            #-------------------------
            #-------------------------                
            cv2.waitKey(1)
            #-------------------------                
            #-------------------------                
            #front.dumpFrame()#bug show frame is normally fetched
        except Exception as e:
            logging.debug('Error {}'.format(e))
    
    logging.info('%d frame has done'%n)
    
    
    lastFrame=front.frame
    front.dumpFrame(direct='./faceDumped/')
    testWin.show(lastFrame)
    
    front.stop()
    testWin.destroyWindow()

if __name__=='__main__':
    main()

