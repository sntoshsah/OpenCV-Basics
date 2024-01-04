import numpy as np
import cv2 as cv


img = cv.imread('./index3.jpeg')
b, g, r = cv.split(img)
zeros = np.zeros(img.shape[:2], dtype="uint8") # Black image
ones = 255*np.ones(img.shape[:2], dtype="uint8") # White image

cv.imshow("Original", img)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)
print(f'Image shape: {img.shape}')

print(f'b shape: {b.shape}')
print(f'g shape: {g.shape}')
print(f'r shape: {r.shape}')

cv.imshow('Merged', cv.merge([r, g, b]))

cv.imshow('red', cv.merge([zeros, zeros, r]))
cv.imshow('green', cv.merge([zeros, g, zeros]))
cv.imshow('blue', cv.merge([b, zeros, zeros]))

cv.imshow('white', ones)
cv.imshow('black', zeros)

print(ones)

print(zeros)

cv.waitKey(0)
cv.destroyAllWindows()  