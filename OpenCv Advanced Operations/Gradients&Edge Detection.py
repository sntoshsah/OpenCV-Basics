import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('cat.jpeg')
cv.imshow('image', img)

'''
# Laplacian Gradients

It calculates the Laplacian of the image given by the relation, 
Δsrc=(∂2src/∂x2)+(∂2src/∂y2) 
where each derivative is found using Sobel derivatives.
If ksize = 1, then following kernel is used for filtering:
    1 0 0
    1 -4 1
    0 1 0
cv.Laplacian()
# Sobel and Scharr Gradients
Sobel operators is a joint Gaussian smoothing plus differentiation operation, so it is more resistant to noise. 
You can specify the direction of derivatives to be taken, vertical or horizontal (by the arguments, yorder and xorder respectively).
You can also specify the size of kernel by the argument ksize. If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter

cv.Sobel()
cv.Scharr()

'''

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx, sobely)

scharrx = cv.Scharr(gray, cv.CV_64F, 1, 0)
scharry= cv.Scharr(gray, cv.CV_64F, 0, 1)
scharrcombined = cv.bitwise_or(scharrx, scharry)

cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('combined', combined)

cv.imshow('scharrx', scharrx)
cv.imshow('scharry', scharry)
cv.imshow('Scharrcombined', scharrcombined)


cv.waitKey(0)
cv.destroyAllWindows()