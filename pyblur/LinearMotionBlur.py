# -*- coding: utf-8 -*-
import math
import numpy as np
import cv2



def LinearMotionBlur_random(img,length_span, theta_span):
    if type([]) != type(length_span):
        raise Exception("length_span should be list")
    if type([]) != type(theta_span):
        raise Exception("length_span should be list")
    if theta_span.max() >= 180:
        raise Exception('max angle should be less than 180')

    length = np.random.randint(length_span)
    angle = np.random.randint(theta_span)
    return LinearMotionBlur(img, lineLength, angle)

def LinearMotionBlur(img, dim, angle):
    imgarray = np.array(img, dtype="float32")
    kernel = getBlurKernel(dim, angle)
    BlurImg = cv2.filter2D(imgarray, -1, kernel).astype("uint8")
    return BlurImg

def getBlurKernel(length, theta):
    if length % 2 == 0:
        raise Exception("length should be odd!", length)
    kernel = np.zeros([length, length])
    kernel[math.floor(length/2),:] = 1
    mask = cv2.getRotationMatrix2D((length/2,length/2),theta,1)
    kernel = cv2.warpAffine(kernel, mask, (length, length))
    kernel = kernel / kernel.sum()
    return kernel