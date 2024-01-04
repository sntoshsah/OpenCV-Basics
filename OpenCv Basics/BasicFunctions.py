import cv2 as cv



# Read an image
img = cv.imread('index3.jpeg')
cv.imshow('image', img)

# Changing colorspaces
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # cvtColor(src, code[, dst[, dstCn]])
cv.imshow('Gray', gray)

Hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', Hsv)


# Blur
blur = cv.blur(img, (5,5), cv.BORDER_DEFAULT) # GaussianBlur(src, ksize, sigmaX) ksize is kernel size
cv.imshow('Simple Blur on real image', blur)
grayBlur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) # GaussianBlur(src, ksize, sigmaX) ksize is kernel size
cv.imshow('Gaussian Blur on gray image', grayBlur)

# Blur method
''' 1. cv.blur(img, ksize)
    2. cv.medianBlur(img, ksize) Note:- Its kernel size should be a positive odd integer.ls
    
    3. cv.bilateralFilter(img, d, sigmaColor, sigmaSpace)
    4. cv.GaussianBlur(img, ksize, sigmaX)
    5. cv.boxFilter(img, d, ksize, normalize) '''


# Edge cascade
canny = cv.Canny(img, 125, 175) # Canny(src, threshold1, threshold2)
cv.imshow('Canny', canny)

cannyblur = cv.Canny(grayBlur, 125, 175) # Canny(src, threshold1, threshold2)
cv.imshow('CannyBlur', cannyblur)

''' Cascade Method
1. cv.Canny(img, threshold1, threshold2)
2. cv.Laplacian(img, ddepth, ksize)
3. cv.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)
'''


# Dilating
dilated = cv.dilate(cannyblur, (4,4), iterations=3) # dilate(src, kernel, iterations) increase the thickness
cv.imshow('Dilated', dilated)


# Eroding
eroded = cv.erode(dilated, (4,4), iterations=3) # erode(src, kernel, iterations) decrease the thickness
cv.imshow('Eroded', eroded) 


# Resize
Resizes = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resizes', Resizes)

# Cropping
cropped = Resizes[200:400, 300:400]
cv.imshow('Cropped', cropped)







cv.waitKey(0)
cv.destroyAllWindows