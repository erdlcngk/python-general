# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:08:39 2022

@author: Erdal
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.png", 0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

# harris corner detection
dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")

dst = cv2.dilate(dst, None)
img[dst>0.2*dst.max()] = 1
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")

# shi tomasi detection
img = cv2.imread("sudoku.png", 0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 1000, 0.01, 10)

corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, (125,125,125), cv2.FILLED)
    
plt.figure(), plt.imshow(img), plt.axis("off")