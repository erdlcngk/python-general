import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("resim.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

edges = cv2.Canny(image = img, threshold1 = 0, threshold2 = 255)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")

med_val = np.median(img)
print(med_val)

low = int(max(0,(1-0.33)*med_val))
high = int(min(255,(1+0.33)*med_val))

print(low , "\n", high)

edges = cv2.Canny(image = img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")



# blur
blurred_img = cv2.blur(img, ksize = (2,2))
# ksize (kernel size) arttırıldıkça resimdeki elde edilen detay düşecektir.

med_val = np.median(blurred_img)
low = int(max(0,(1-0.33)*med_val))
high = int(min(255,(1+0.33)*med_val))

edges = cv2.Canny(image = blurred_img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")

