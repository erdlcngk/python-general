# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 03:33:49 2022

@author: Erdal
"""
# %% ilk figür oluşturma
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])
    
plt.figure()
plt.plot(x, y, color = "red", alpha = 0.5, label = "line")
plt.scatter(x, y, color = "blue", alpha = 0.8, label = "scatter")
plt.title("deneme")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.xticks([0,1,2,3,4,5])
plt.legend()

# %% rastgele resim
plt.figure()
img = np.random.random((50,50))
plt.axis("off")
plt.imshow(img,cmap ="gray")
plt.show()
