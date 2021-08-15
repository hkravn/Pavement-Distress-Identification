############################################
# Authors Name: AKM (Avinash Kumar Mishra)
# Description: Code to Quantify the various distress identified through ML Model
# Inputs Required: Frame Refrence No, Bounding Box Coordinates
# Copyright License: GNU GPLv3
############################################

############################################
# Source: https://github.com/shomnathsomu/crack-detection-opencv/blob/master/CrackDetection.py
############################################

from posixpath import basename, split
import cv2
import os
import numpy as np
from numpy.core.numeric import ones

frames = {"01 (1).png", "01 (2).png", "01 (3).png", "01 (4).png", "01 (5).png", "01 (6).png", "01 (7).png", "01 (8).png", "01 (9).png", "01 (10).png", "01 (11).png", "01 (12).png", "01 (13).png", "01 (14).png", "01 (15).png", "01 (16).png"}
basepath = os.path.abspath(os.getcwd())

def crack_qty (frames):
    for frame in frames:
        #Read Image
        loc = basepath + "\\" + frame
        img = cv2.imread(loc, cv2.IMREAD_GRAYSCALE)
        # Image Smoothing
        blur = cv2.blur(img, (2,2))
        #Logarithmic Transform
        img_log = (np.log(blur+1)/np.log(1+np.max(blur)))*255
        img_log = np.array(img_log, dtype=np.uint8)
        #Image Smoothing
        bilateral = cv2.bilateralFilter(img_log, 5, 75, 75)
        #Canny Edge
        edges = cv2.Canny(bilateral, 100, 200)
        #Morphological Closing Operator
        kernel = np.ones((5,5), np.uint8)
        closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
        #Feature Detecting Method
        orb = cv2.ORB_create(nfeatures=1500)
        #Make featured Image
        keypoints, descriptors = orb.detectAndCompute(closing, None)
        featuredImg = cv2.drawKeypoints(closing, keypoints, None)
        #File Name Generate
        frame = frame.split('.')[0] + "_ch_." + frame.split('.')[1]
        #Output Image
        cv2.imwrite(frame, featuredImg)
    return 1

def pothole_vol (frame, coordinates):
    return frame*coordinates

crack_qty(frames)
