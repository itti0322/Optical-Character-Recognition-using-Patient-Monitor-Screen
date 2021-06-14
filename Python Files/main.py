# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:47:31 2021

@author: Irtza
"""
from libraries import *
from getFrame import *
from pre_processing import *
from OCR_implementation import *
from create_dataframe import *
reader=easyocr.Reader(['en'])

import_libraries()

def main():
    prompter = promptlib.Files()
    file_name = prompter.file()
    sec = 0
    frameRate = 1 #//it will capture image in each 1 second
    count=1
    success = getFrame(sec,file_name,count)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec,file_name,count)
        
    print("Framing done")
    image_header=cv2.imread(r'E:\MS 4th Semester\Thesis\1st Meeting (8th Jan)\Syed Irtza Akhtar Bukhari - OCR patient monitor\irtza\frames200.jpg')
    hsv_frame=hsv_conversion(image_header)
    green=get_green_mask(hsv_frame,image_header)
    red=get_red_mask(hsv_frame,image_header)
    yellow=get_yellow_mask(hsv_frame,image_header)
    white=get_white_mask(hsv_frame,image_header)
    header_green=OCR_header(color=green)
    header_red=OCR_header(color=red)
    header_yellow=OCR_header(color=yellow)
    header_white=OCR_header(color=white)
    
    df_red,hd_red=get_headers_dataframe(header_red)
    df_yellow,hd_yellow=get_headers_dataframe(header_yellow)
    df_white,hd_white=get_headers_dataframe(header_white)
    df_green,hd_green=get_headers_dataframe(header_green)
    
    
    for infile in sorted(glob.glob(r'E:\MS 4th Semester\Thesis\1st Meeting (8th Jan)\Syed Irtza Akhtar Bukhari - OCR patient monitor\irtza\*.jpg'), key=numericalSort):
        image = cv2.imread(infile)

        hsv_frame=hsv_conversion(image)
        green=get_green_mask(hsv_frame,image)
        red=get_red_mask(hsv_frame,image)
        yellow=get_yellow_mask(hsv_frame,image)
        white=get_white_mask(hsv_frame,image)
        
        green_value=OCR_values(green)
        red_value=OCR_values(red)
        yellow_value=OCR_values(yellow)
        white_value=OCR_values(white)
        
        df_green=df_values(df_green,hd_green,green_value)
        df_red=df_values(df_red,hd_red,red_value)
        df_yellow=df_values(df_yellow,hd_yellow,yellow_value)
        df_white=df_values(df_white,hd_white,white_value)

    dataframe=pd.concat([df_green,df_yellow,df_red,df_white],axis=1)    
    dataframe.to_csv('Output.csv',index=False)
    return dataframe

dataframe=main()



