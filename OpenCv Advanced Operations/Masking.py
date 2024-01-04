import cv2 as cv
import numpy as np


img = cv.imread('./opencv.png')
cv.imshow('image', img)

mask = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow('mask', mask)

cv.rectangle(mask, (23, 145), (150, 200), 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('And masked', masked)

masked2 = cv.bitwise_or(img,img,mask=mask)
cv.imshow('OR masked2', masked2)

masked3 = cv.bitwise_not(img,img,mask=mask)
cv.imshow(' Not masked3', masked3)


cv.waitKey(0)
cv.destroyAllWindows()