# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:27:15 2022

@author: Erdal
"""

import cv2
import numpy as np

img = cv2.imread("lenaYamuk.jpg")
cv2.imshow("lena",img)

widht = 400
height = 500

pts1 = np.float32([[1,1],[1,412],[412,1],[412,412]])
pts2 = np.float32([[0,0],[0,height],[widht,0],[widht,height]])

matris = cv2.getPerspectiveTransform(pts1, pts2)
print(matris)

imgOutPut = cv2.warpPerspective(img, matris, (widht,height))
cv2.imshow("OutPut", imgOutPut)