# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:06:22 2021

@author: Irtza
"""

def hsv_conversion(image):
    hsv_frame=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    return hsv_frame

def get_green_mask(hsv_frame,image):
    low_green=np.array([50, 25, 25])
    high_green=np.array([70, 255,255])
    mask_green=cv2.inRange(hsv_frame,low_green,high_green)
    green=cv2.bitwise_and(image,image,mask=mask_green)
    return green

def get_yellow_mask(hsv_frame,image):
    low_yellow=np.array([25, 80, 80])
    high_yellow=np.array([40, 255, 255])
    mask_yellow=cv2.inRange(hsv_frame,low_yellow,high_yellow)
    yellow=cv2.bitwise_and(image,image,mask=mask_yellow)
    return yellow

def get_red_mask(hsv_frame,image):
    low_red1=np.array([0, 70, 50])
    high_red1=np.array([10, 255, 255])
    low_red2=np.array([170, 70, 50])
    high_red2=np.array([180, 255, 255])

    mask_red1=cv2.inRange(hsv_frame,low_red1,high_red1)
    mask_red2=cv2.inRange(hsv_frame,low_red2,high_red2)
    mask_red=mask_red1|mask_red2
    red=cv2.bitwise_and(image,image,mask=mask_red)
    return red

def get_white_mask(hsv_frame,image):
    low_white=np.array([0, 0, 168])
    high_white=np.array([172, 111, 255])
    mask_white=cv2.inRange(hsv_frame,low_white,high_white)
    white=cv2.bitwise_and(image,image,mask=mask_white)
    return white

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts