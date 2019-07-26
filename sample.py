import cv2
import numpy as np


img = cv2.imread('image.jpg', 0)

img = img[9 : 18, 0 : 9]

print(img.shape)