# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:05:18 2021

@author: Irtza
"""

def getFrame(sec,file_name,count):
    vidcap = cv2.VideoCapture(file_name)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(r"E:\MS 4th Semester\Thesis\1st Meeting (8th Jan)\Syed Irtza Akhtar Bukhari - OCR patient monitor\irtza\frames"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames