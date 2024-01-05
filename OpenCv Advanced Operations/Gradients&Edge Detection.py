import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('cat.jpeg')
cv.imshow('image', img)


cv.waitKey(0)
cv.destroyAllWindows()