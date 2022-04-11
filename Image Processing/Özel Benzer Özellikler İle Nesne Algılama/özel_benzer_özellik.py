# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:29:31 2022

@author: Erdal


1-) Veri seti:
    negatif ve pozitif resimler olacak (negatif resimler
    tespit edilmek istenemeyen, pozitif resimler tespit 
    edilmek istenen resimler olacak)
    
2-) cascade programı indirilecek

3-)Bu programı kullanarak cascade oluşturulacak

4-) cascade kullanarak tespit algoritması yazılacak
"""
import cv2
import os
# resim depo klasörü
path = "images"

# resim boyutu
imgWidht = 180
imgHeight = 120

# video capture
cap = cv2.VideoCapture(0)
# burada yapılan ayarlarda 3'e karşılık gelen parametre genişlik
# 4'e karşılık gelen parametre yüksekliktir
# 10'a karşılık gelen değer kameranın aydınlık değeridir.
cap.set(3,640)
cap.set(4,480)
cap.set(10,180)

# klasör oluşturma
global countFolder
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path + str(countFolder))
    
saveDataFunc()

count = 0
countSave = 0

while True:
    success, img = cap.read()
    
    if success:
        img = cv2.resize(img, (imgWidht, imgHeight))
        
        if count % 5 == 0:
            cv2.imwrite(path + str(countFolder) + "/" + str(countSave) + "_" + ".png", img)
            countSave += 1
            print(countSave)
        count += 1
        
        cv2.imshow("Image", img)
        
        if cv2.waitKey(1) & 0xFF == ord ("q"):
            break

cap.release()
cv2.destroyAllWindows()      

# BUraya kadar kameradan resimleri alıp bir dosyaya kaydeden bir programdır.
            
            
            
            
            
            
            