# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:02:11 2022

@author: elyes
"""

import os
import csv
def get_t2_end(file_name):
    BASE_DIR="./embryo_dataset_annotations"
    file_path=os.path.join(BASE_DIR,file_name)
    with open(file_path,'r') as f:
       csv_reader=csv.reader(f) 
       for row in csv_reader:
           if row[0]=='t2':
               return int(row[2])
    return 0   

    
def remove_extra_frames():
    BASE_DIR="./embryo_dataset"
    for dir in os.listdir(BASE_DIR):
        file_name=dir+'_phases.csv'
        t2_end=get_t2_end(file_name)
        frames_dir=os.path.join(BASE_DIR,dir,'F0')
        frames_list=sorted(os.listdir(frames_dir),key=len)
        for frame in frames_list[t2_end-1:]:
            if os.path.exists(os.path.join(frames_dir,frame)):
                os.remove(os.path.join(frames_dir,frame))
# remove_extra_frames()

if __name__=="__main__":
    remove_extra_frames()


    