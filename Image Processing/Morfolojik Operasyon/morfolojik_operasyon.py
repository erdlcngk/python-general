# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 12:28:32 2022

@author: Erdal
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("resim.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("orijinal")

# %% erozyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("erozyon")

# %% genişleme (dilation)
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("genişleme")

# %% beyaz gürültü
whiteNoise = np.random.randint(0,2,size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("beyaz gürültü")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("beyaz gürültülü resim")

# %% açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("açılma uygulanmış resim")

# siyah gürültü
blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = whiteNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("siyah gürültü")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("siyah gürültü")

# kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("siyah gürültüden arındırma")

# gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("gradyanlı resim")

