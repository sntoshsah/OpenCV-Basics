import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('./index4.jpeg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('cannyrgb', canny)

cannygray = cv.Canny(gray, 125, 175)
cv.imshow('cannyGray', canny)


blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

cannyblur = cv.Canny(blur, 125, 175)
cv.imshow('cannyblur', cannyblur)

# contours on canny images

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # findContours(image, mode, method) # contour is applied on canny edge detected image for best result.
cv.drawContours(img, contours, -1, (0,255,0), 2) # drawContours(image, contours, contourIdx, color, thickness)
cv.imshow('contours drawn', img)


contoursblur, hierarchiesblur = cv.findContours(cannyblur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(cannyblur, contoursblur, -1, (0,255,0), 2)
cv.imshow('contoursblur drawn', img)

# contour on threshold images
ret,thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thres', thres)

ret,thresblur = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
cv.imshow('thres blur', thresblur)


contoursthes, hierarchiesthres = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contoursthes, -1, (0,255,0), 2)
cv.imshow('contours drawn', img)    

contoursthesblur, hierarchiesthresblur = cv.findContours(thresblur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blur, contoursthesblur, -1, (0,255,0), 2)
cv.imshow('contours Thres drawn', blur)    





print(f'{len(contours)} contour(s) found! on canny images')
print(f'{len(contoursblur)} contour(s) found! on canny blur images')

print(f'{len(contoursthes)} contour(s) found! on threshold  images')
print(f'{len(contoursthesblur)} contour(s) found! on threshold blur images')


# print(hierarchies)
# print(hierarchiesblur)


cv.waitKey(0)
cv.destroyAllWindows()

