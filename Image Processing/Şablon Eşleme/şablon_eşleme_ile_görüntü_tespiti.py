# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 00:36:49 2022

@author: Erdal
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("kedi.jpg", 0)
print(img.shape)

template = cv2.imread("kedi1.png", 0)
print(template.shape)
h, w = template.shape

methods = ["cv2.TM_CCOEFF", "cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR",
           "cv2.TM_CCORR_NORMED", "cv2.TM_SQDIFF", "cv2.TM_SQDIFF_NORMED"]

for method in methods:
    meth = eval(method) # 'cv2.TM_CCOEFF' -> cv2.TM_CCOEFF şekline çevriliyor.
    
    result = cv2.matchTemplate(img, template, meth)
    print(result.shape)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if meth in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc # method yazımlarından dolayı üstteki iki methodun
                           # yazımında minimum locationlar sol üste denk gelmektedir
                           # aşağıda ise tam tersidir.
    else:
        top_left = max_loc
    
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    
    plt.figure()
    plt.subplot(121), plt.imshow(result, cmap = "gray")
    plt.title("Eşleşen Sonuç"), plt.axis("off")
    plt.subplot(122), plt.imshow(img, cmap = "gray")
    plt.title("Tespit Edilen Sonuç"), plt.axis("off")
    plt.suptitle(meth)
    
    plt.show()