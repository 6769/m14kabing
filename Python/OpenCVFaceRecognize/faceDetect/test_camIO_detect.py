# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:33:35 2016

test FaceDetectation

@author: pip
"""

import cv2
import logging
from cameraIO import IOSteam
import sys


from trackers import FaceTracker

front=IOSteam()
tracker=FaceTracker()

front.run()
tracker.update( front.frame)
facelist=tracker.faces
front.stop()
print(facelist)

