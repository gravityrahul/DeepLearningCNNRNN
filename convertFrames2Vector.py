__file__ = 'convert2Frames.py'

import os

filePath=os.path.realpath(__file__)
BASE_DIR=filePath.split(__file__)[0]

import tensorflow as tf
from PIL import Image
import glob
import pandas as pd
import numpy as np

def convertImageToVector(image_directory, IMAGE_WIDTH=256, IMAGE_HEIGHT=256, scale='RGB'):
    files_ = glob.glob(os.path.join(image_directory + '/*.jpg'))
    images_list = [Image.open(frame_) for frame_ in files_]
    if scale=='RGB':
        # Convert the images to 256 x 256 pixels in RGB mode
        images_list_256=[img.resize((IMAGE_WIDTH, IMAGE_HEIGHT), 3) for img in images_list]
        images_256_float_list=[tf.image.convert_image_dtype(img_, tf.float32) for img_ in images_list_256]

    print ("Converted %d images to tensor flow stacked object" %len(images_256_float_list))
    images_stacked_vector = tf.stack(images_256_float_list, axis=0)
    print ("###########################################################################")
    print (images_stacked_vector.shape)
    print ("###########################################################################")

    return images_stacked_vector



def npsaveCompressedFiles(pathToDir, videoDirName):
    imagesDir=os.path.realpath(os.path.join(pathToDir, videoDirName))
    destination_folder=os.path.realpath(os.path.join(BASE_DIR, 'npz_data'))
    if os.path.exists(destination_folder):
        pass
    else:
        os.makedirs(destination_folder)

    tensorFlowObject = convertImageToVector(imagesDir)
    with tf.Session() as sess:
        tfData=tensorFlowObject.eval()
    np.savez(os.path.join(destination_folder, videoDirName), x=tfData)



if __name__ == "__main__":
    pathToDir='train_data'
    dirs_ = os.listdir(os.path.join(BASE_DIR, pathToDir))
    for videoDir in dirs_:
        print ("Converting Image to Vector for %s" %videoDir)
        npsaveCompressedFiles(pathToDir, videoDir)
