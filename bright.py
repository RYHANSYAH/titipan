import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def bright(image,factor):
    bright_image = image.astype(np.float32)
    bright_image = bright_image + factor 

    bright_image = np.clip (bright_image,0,255)

    return bright_image.astype(np.uint8)

image = img.imread("C:\\Users\\KOMPUTER JARKOM 28\\Downloads\\Nega.png")
br_image = bright (image,150)

plt.figure(figsize=(9,5))
plt.subplot(2,2,1)
plt.imshow(image)
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(br_image)
plt.axis("off")

plt.show()