import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img = cv.imread('./index3.jpeg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('bgr2gray', gray)

bgr = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imshow('rgb2bgr', bgr)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('bgr2hsv', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('bgr2lab', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('bgr2rgb', rgb)

bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab2bgr', bgr)

bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv2bgr', bgr)

bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray2bgr', bgr)

# hsv = cv.cvtColor(gray, cv.COLOR_GRAY2HSV) # Can't convert gray to hsv, can only convert gray to bgr to hsv
# cv.imshow('gray2hsv', hsv)

rgb = cv.cvtColor(gray, cv.COLOR_GRAY2RGB)
cv.imshow('gray2rgb', rgb)

# lab = cv.cvtColor(gray, cv.COLOR_GRAY2LAB)  # Can't convert gray to hsv, can only convert gray to bgr to hsv
# cv.imshow('gray2lab', lab)


cv.waitKey(0)
cv.destroyAllWindows