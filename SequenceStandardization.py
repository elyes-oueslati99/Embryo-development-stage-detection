import numpy as np
import csv
import shutil
import os
from tqdm import tqdm


def get_sorted_frames(sequence_dir):
    path=os.path.join(sequence_dir,'F0')
    frames_list=sorted(os.listdir(path),key=len)
    return(frames_list)


def remove_excess_frames(dataset_path,target_path):
    if os.path.exists(target_path)==False:
        os.mkdir(target_path)

    for dir in tqdm(os.listdir(dataset_path)):
        frames_list=get_sorted_frames(os.path.join(dataset_path,dir))
        for file in frames_list[:120]:
            if os.path.exists(os.path.join(target_path,dir))==False:
                os.mkdir(os.path.join(target_path,dir))
            shutil.copyfile(os.path.join(dataset_path,dir,'F0',file), os.path.join(target_path,dir,file))




if __name__=="__main__":
    dataset_path='.\embryo_dataset'
    target_path='.\standard_dataset'
    remove_excess_frames(dataset_path,target_path)

    
