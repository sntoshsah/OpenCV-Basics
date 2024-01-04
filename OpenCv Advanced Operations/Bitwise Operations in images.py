import cv2 as cv
import numpy as np


black =np.zeros((500,500),dtype='uint8')
# cv.imshow('Black',black)

circle = cv.circle(black, (250,250), 50, (255,255,255), -1) # circle(center, radius, color, thickness)
cv.imshow('White circle',circle)

rectangle = cv.rectangle(black, (210,200), (290,300), (255,255,255), -1) # rectangle(start_point, end_point, color, thickness)
cv.imshow('White Rectangle ',rectangle)

bitwiseAnd = cv.bitwise_and(rectangle, circle) # bitwise_and(src1, src2) # Union of two images
cv.imshow('And',bitwiseAnd)

bitwiseOr = cv.bitwise_or(rectangle, circle) # bitwise_or(src1, src2) # Intersection of two images
cv.imshow('Or',bitwiseOr)

bitwiseXor = cv.bitwise_xor(rectangle, circle) # bitwise_xor(src1, src2) # Symmetric difference i.e difference of intersection and union, Union - Intersection
cv.imshow('Xor',bitwiseXor)

bitwiseNot = cv.bitwise_not(rectangle)
cv.imshow('Not',bitwiseNot)

cv.waitKey(0)
cv.destroyAllWindows()