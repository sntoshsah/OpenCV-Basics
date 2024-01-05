import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('./village2.jpeg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# Simple Thresholding

ret, thresh = cv.threshold(gray, 127, 200, cv.THRESH_BINARY) # threshold(src, thresh, maxval, type)
cv.imshow('Binary thresh', thresh)

ret, thresh2 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh_Binary_Inv', thresh2)

ret, thresh3 = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)
cv.imshow('thresh_Trunc', thresh3)

ret, thresh4 = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
cv.imshow('thresh_Tozero', thresh4)

ret, thresh5 = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO_INV)
cv.imshow('threshTozero_Inv', thresh5)



# Adaptive Thresholding

adaptive_thresh_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) 
# adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
cv.imshow('adaptive_thresh', adaptive_thresh_mean)

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow('adaptive_thresh_gaussian', adaptive_thresh_gaussian)

adaptive_thresh_gaussian_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
cv.imshow('adaptive_thresh_gaussian_inv', adaptive_thresh_gaussian_inv)

adaptive_thresh_mean_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 2)
cv.imshow('adaptive_thresh_mean_inv', adaptive_thresh_mean_inv)

# adaptive_thresh_otsu = cv.threshold(gray,0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# cv.imshow('adaptive_thresh_otsu', adaptive_thresh_otsu)






cv.waitKey(0)
cv.destroyAllWindows()