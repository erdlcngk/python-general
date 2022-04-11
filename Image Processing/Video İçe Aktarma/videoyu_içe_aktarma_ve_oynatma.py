# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:11:28 2022

@author: Erdal
"""

import cv2
import time

# video ismi
video_name = "highway.mp4"

# videoyu içe aktar: capture, cap
cap = cv2.VideoCapture(video_name)

print("genişlik:", cap.get(3), "yükseklik:", cap.get(4))

if cap.isOpened() == False:
    print("Hata")
    
while True:
    ret, frame = cap.read() #read() methodu 2 değer dönüyor, bir tanesi görüntünün okunup okunamadığı hakkında 

    
    if(ret == True):
        cv2.imshow("Video", frame)
        time.sleep(0.01)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
   

cap.release()
cv2.destroyAllWindows()