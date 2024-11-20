import cv2
import numpy as np 
image = cv2.imread('img.jpeg')
grayimg = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grayimg) # making dark areas light and light areas dark.
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grayimg , invertedblur, scale=256.0)
resizedimg = cv2.resize(sketch, (500,500))
cv2.imshow('output', resizedimg)
cv2.waitKey(0)