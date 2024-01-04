import cv2 as cv
import numpy as np


img = cv.imread('./paint1.jpeg')
cv.imshow('image', img) 
"""_summary_
    cv.GaussianBlur(src, ksize, sigmaX)
    cv.medianBlur(src, ksize)
    cv.bilateralFilter(src, d, sigmaColor, sigmaSpace)
    cv.blur(src, ksize) # mean filtering
    """
    
    
cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # Kernel size must be odd
cv.imshow('Gaussian Blur', img)

cv.blur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', img)

cv.medianBlur(img, 7)
cv.imshow('Median Blur', img)

cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Filter', img)





cv.waitKey(0)
cv.destroyAllWindows()