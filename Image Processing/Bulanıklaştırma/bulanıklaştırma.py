# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:14:57 2022

@author: Erdal
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# bluring (detayı azaltır ve gülürtüyü engeller)
img = cv2.imread("orman.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img), plt.axis("off"), plt.title("orijinal"), plt.show()

# ortalama bulanıklaştırma yöntemi
dst2 = cv2.blur(img,ksize = (3,3))
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("ortalama blur")

# gauss blur
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("gauss blur")

# medyan blur
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("medyan blur")

# %% gürültü ekleme ve blurla gürültüyü azaltma
def gaussianNoise(image):
    row, col, ch = img.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    
    return noisy

# içe aktar ve normalize et
img = cv2.imread("orman.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255

plt.figure()
plt.imshow(img), plt.axis("off"), plt.title("orijinal"), plt.show()

gaussianNoiseImg = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoiseImg),plt.axis("off"),plt.title("gauss blurlu resim")

# gauss blur
gb = cv2.GaussianBlur(gaussianNoiseImg, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("gauss blur uygulanmış resim")

# %% tuz karabiber gürültüsü ekleme ve gürültüyü azaltma
def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    
    noisy = np.copy(image)
    
    # salt beyaz
    np_salt = np.ceil(amount*image.size*s_vs_p)
    coords = [np.random.randint(0, i-1, int(np_salt)) for i in image.shape]
    noisy[coords] = 1
    
    # pepper siyah
    np_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i-1, int(np_pepper)) for i in image.shape]
    noisy[coords] = 0
    return noisy

spImage = saltPepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("tuz biber blur")

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("median blur uygulanmış resim")






