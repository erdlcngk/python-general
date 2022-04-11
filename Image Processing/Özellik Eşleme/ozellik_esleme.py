# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:45:58 2022

@author: Erdal
"""

import cv2
import matplotlib.pyplot as plt

chos = cv2.imread("cikolatalar.jpg", 0)
cho = cv2.imread("nestle.jpg", 0)

# orb tanımlayıcı
# köşe, kenar gibi nesneye ait özellikler
orb = cv2.ORB_create()

# anahtar nokta tespiti
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

# brute force eşleme
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# noktaları eşleştir
matches = bf.match(des1, des2)

# mesafeye göre sırala
matches = sorted(matches, key = lambda x: x.distance)

# eşleşen resimleri görselleştirme
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags = 2)
plt.imshow(img_match), plt.axis("off"), plt.title("orb")

# sift tanımlayıcısı
sift = cv2.xfeatures2d.SIFT_create()

# bf eşlemeyi yeniden tanımlıyoruz
bf = cv2.BFMatcher()

# anahtar nokta tespiti : sıft ile
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(chos, None)

matches = bf.knnMatch(des1, des2, k = 2)

guzel_eslesme = []

for match1, match2 in matches:
     if match1.distance < 0.75 * match2.distance:
         guzel_eslesme.append([match1])
         
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, guzel_eslesme, None, flags = 2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("sift")











