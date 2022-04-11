# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:41:41 2022

@author: Erdal
"""

import cv2
import os

# resimleri çoklu içe aktarma
files = os.listdir()
print(files)

img_path_list = []

for f in files:
    if(f.endswith(".jpg")):
        img_path_list.append(f)

for j in img_path_list:
    print(j)
    image = cv2.imread(j)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    # bütün kediler bu oranlarla tespit edilebiliyor. En iyi sonuç için, 
    # minNeighbors ve scaleFactor ile belirli oranlarda oynamak gerekiyor.
    rects = detector.detectMultiScale(gray, minNeighbors = 8, scaleFactor = 1.0379)
    
    for (i,(x,y,w,h)) in enumerate(rects):
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 10)
        #.putText(resim, yazı, koordinat, font, kalınlık, renk)
        cv2.putText(image, f"Kedi{i+1}", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.55 ,(0,255,255), 2)
    
    cv2.imshow(j, image)
    if(cv2.waitKey(0) & 0xFF == ord("q")):
        continue
    








