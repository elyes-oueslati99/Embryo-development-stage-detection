# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:41:24 2022

@author: elyes
"""

import os

def keep_last50(directory):
    frames_list=sorted(os.listdir(directory),key=len)
    for frame in frames_list[:70]:
        frame_path= os.path.join(os.path.join(directory,frame))
        if os.path.exists(frame_path):
            os.remove(frame_path)

BASE_DIR="./To-upload2/"
for directory in os.listdir(BASE_DIR):
    directory_path=os.path.join(BASE_DIR,directory)
    keep_last50(directory_path)

# directory="ZS435_EMB6_DISCARD/"


    
    