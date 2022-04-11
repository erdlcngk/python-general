# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:11:00 2022

@author: Erdal
"""

import cv2
import numpy as np

# resmi içe aktar
img = cv2.imread("lena.jpg")
cv2.imshow("orijinal", img) 

# %% dikey birleştirme (resmi boy kısımlarından birleştirir)
hor = np.hstack((img,img))
cv2.imshow("dikey birlestirilmis", hor)

# %% yatay birleştirme (resmi en kısımlarından birleştirir)
ver = np.vstack((img,img))
cv2.imshow("yatay birlesitilmis", ver)
