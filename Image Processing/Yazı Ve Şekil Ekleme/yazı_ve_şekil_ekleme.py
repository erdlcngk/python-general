# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:04:30 2022

@author: Erdal
"""

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # siyah bir resim
print(img.shape)

cv2.imshow("siyah", img)

# %% çizgi
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (100,100),(100,300),(0,255,0),3) # (BGR = (0,255,0) => Yeşil)
cv2.imshow("cizgili resim", img)

# %% dikdörtgen
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED)
cv2.imshow("dikdortgenli resim", img)

# %% çember, daire
#(resim, merkez, yarıçap, renk, kalınlık)
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow("cemberli resim", img)

# %% metin
# (resim, başlangıç notkası, font, kalınlık, renk)
cv2.putText(img,"RESIM", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("cemberli resim", img)