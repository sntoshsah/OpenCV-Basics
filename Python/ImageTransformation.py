import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('./index2.jpeg')
cv.imshow('image', img)

def Translate(img, x, y):
    """
    Translate the given image by the specified amount in the x and y directions.

    Parameters:
        img (numpy.ndarray): The input image to be translated.
        x (int): The amount of translation in the x direction. -ve for left, +ve for right
        y (int): The amount of translation in the y direction. -ve for up, +ve for down

    Returns:
        numpy.ndarray: The translated image.
    """
    transMat = np.float32([[1,0,x],
                           [0,1,y]])
    
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translateImg=Translate(img, 74, 50)
cv.imshow('Translated', translateImg)


def rotate(img, angle, rotPoint=None):
    """
    Rotate the given image around the given rotation point.

    Parameters:
        img (numpy.ndarray): The image to be rotated.
        angle (int): The angle of rotation in degrees. +ve for anti-clockwise, -ve for clockwise
        rotPoint (tuple, optional): The rotation point. Defaults is None.

    Returns:
        numpy.ndarray: The rotated image.
    """
    (h, w) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (w//2, h//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # getRotationMatrix2D(center, angle, scale)
    dimensions = (w, h)
    return cv.warpAffine(img, rotMat, dimensions)

rotateImage = rotate(img, -45)
cv.imshow('Rotated', rotateImage)

rotate2Image = rotate(rotateImage, -45)
cv.imshow('Rotated2', rotate2Image)

rotate2Image = rotate(img, -90)
cv.imshow('Rotated 90', rotate2Image)


# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)


# Flipping
flip = cv.flip(img, 1) # flip(src, flipCode) - 0 for vertical, 1 for horizontal as well as -1 for both
cv.imshow('Flipped', flip)


# Cropping
cropped = img[0:50, 75:100]   # img[y1:y2, x1:x2]
cv.imshow('Cropped', cropped)
print(img.shape)
cv.waitKey(0)
cv.destroyAllWindows()