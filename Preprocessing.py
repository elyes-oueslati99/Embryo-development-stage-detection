import numpy as np
import os

from tflite_model_maker.config import ExportFormat, QuantizationConfig
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector
from tflite_support import metadata
import tensorflow as tf
assert tf.__version__.startswith('2')
tf.get_logger().setLevel('ERROR')

from absl import logging
logging.set_verbosity(logging.ERROR)
import DetectionModule
from tqdm import tqdm
from PIL import Image


def Cropping(BASE_DIRECTORY,TARGET_DIRECTORY,TFLITE_MODEL_PATH='cellule_detection.tflite',DETECTION_THRESHOLD=0.5,shape=250):

    for directory in os.listdir(BASE_DIRECTORY):
        t=os.path.join(TARGET_DIRECTORY,directory)
        print(t)
        if os.path.exists(t)==False:
          os.mkdir(t)
        filename_list=list(os.listdir(os.path.join(BASE_DIRECTORY,directory)))
        print(filename_list[0])
        filename_list.sort()
        for filename in tqdm(filename_list):
            f = os.path.join(os.path.join(BASE_DIRECTORY,directory), filename)
            image = Image.open(f).convert('RGB')
            image.thumbnail((512, 512), Image.ANTIALIAS)
            image_np = np.asarray(image)

            options =DetectionModule.ObjectDetectorOptions(
                    num_threads=4,
                    score_threshold=DETECTION_THRESHOLD,
            )

            # Run object detection estimation using the model.
            detector = DetectionModule.ObjectDetector(model_path=TFLITE_MODEL_PATH, options=options)
            detections = detector.detect(image_np)


            #normalise the box
            try:
                cx,cy=((detections[0][0][0]+detections[0][0][2])/2,(detections[0][0][1]+detections[0][0][3])/2)
            except Exception as e: print(e)

            crop_param=(cx-(shape/2),cy-(shape/2),cx+(shape/2),cy+(shape/2))
            image=image.crop(crop_param)
            image=image.save(os.path.join(t,filename),"JPEG")


if __name__=="__main__":
    BASE_DIRECTORY='A to F'
    TARGET_DIRECTORY='Preprocessed_data'
    Cropping(BASE_DIRECTORY,TARGET_DIRECTORY,'cellule_detection.tflite',0.5,250)
