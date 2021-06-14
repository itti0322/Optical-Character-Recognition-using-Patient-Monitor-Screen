# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:11:52 2021

@author: Irtza
"""

def get_mix_strings(item):
    for ch in item:
        if not ch.isalpha():
            if not ch.isdigit():
                return False
    return True

def get_all_num(item):
    return all([ch.isdigit() for ch in item])

def get_all_alpha(item):
    return all([ch.isalpha() for ch in item])

def OCR_header(color):
    result = reader.readtext(color,min_size= 25,detail=0,text_threshold=0.90)
    final_header = []
    for item in result:
        if get_all_num(item):
            continue
        elif get_mix_strings(item):
            final_header.append(item)
        elif get_all_alpha(item):
            final_header.append((item))
            
    return final_header

def OCR_values(color):
    result = reader.readtext(color,min_size= 80,detail=0,text_threshold=0.90)
    value = [x for x in result if any(x1.isdigit() for x1 in x)]
    return value