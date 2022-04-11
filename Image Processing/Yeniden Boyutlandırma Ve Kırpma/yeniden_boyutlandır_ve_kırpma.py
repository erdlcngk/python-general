# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:57:25 2022

@author: Erdal
"""

import cv2

img = cv2.imread("lena.jpg")
print("Resim boyutu: ", img.shape)
cv2.imshow("Orijinal", img)

imgResized = cv2.resize(img,(800,800))
print("Yeniden boyutlandırılmış resim: ", imgResized.shape)
cv2.imshow("Resized img", imgResized)

# kırpma
imgCropped = img[:200,0:300]
cv2.imshow("cropped",imgCropped)