import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('./paint1.jpeg')
cv.imshow('image', img)



# RGB histogram
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.legend(['Blue', 'Green', 'Red'])
plt.title('RGB Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


black = np.zeros(gray.shape[:2], dtype="uint8")
cv.imshow('mask', black)

circle = cv.circle(black, (gray.shape[1]//2-10,gray.shape[0]//2), 25, (255,255,255), -1) # circle(center, radius, color, thickness)  # ROI - Region of Interest
cv.imshow('White circle',circle)


maskedImg = cv.bitwise_and(img, img, mask=circle)  # bitwise_and(src1, src2)
cv.imshow('And masked', maskedImg)



# Gray histogram

gray_hist0 = cv.calcHist([gray], [0], None, [256], [0,256]) # calcHist(images, channels, mask, histSize, ranges)
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist0)
plt.xlim([0,256])
plt.show()


# Gray histogram for masked image

gray_hist1 = cv.calcHist([maskedImg], [0], None, [256], [0,256]) # calcHist(images, channels, mask, histSize, ranges)
plt.figure()
plt.title('Grayscale Histogram for masked image')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist1)
plt.xlim([0,256])
plt.show()


# Color Histogram for masked image

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([maskedImg], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.legend(['Blue', 'Green', 'Red'])
plt.title('RGB Histogram for masked image')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()