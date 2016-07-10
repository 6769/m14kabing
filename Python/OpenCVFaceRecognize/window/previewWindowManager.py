# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:48:05 2016

@author: pip
"""
import cv2
import numpy
import os
import time
import threading


class PreviewWindowManager(object):

    def __init__(self, windowName, keypressCallback = None):
        self.keypressCallback = keypressCallback

        self._windowName = windowName
        self._isWindowCreated = False

    @property
    def isWindowCreated(self):
        return self._isWindowCreated

    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True

    def show(self, frame):
        cv2.imshow(self._windowName, frame)

    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False

    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            # Discard any non-ASCII info encoded by GTK.
            keycode &= 0xFF
            self.keypressCallback(keycode)
            
if __name__=='__main__':
    print('Main')
    randomgf=numpy.random.randint(0,256,120000).reshape(100,400,3)
    testWin=PreviewWindowManager('testWin')
    testWin.createWindow()
    testWin.show(randomgf)
    #testWin.destroyWindow()