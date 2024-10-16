import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\KOMPUTER JARKOM 28\\Downloads\\Nega.png"

image = img.imread(path)
image_neg = 255 - image

r_image = image[:,:,0]
r_neg = image_neg[:,:,0]

hist_r, bins_r = np.histogram(r_image.flatten(), bins = 256, range = [0,256])
hist_r_neg, bins_r_neg= np.histogram(r_neg.flatten(), bins = 256, range = [0,256])
plt.figure(figsize=(15,12))

plt.subplot(2,2,1)
plt.imshow(image)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(image_neg)
plt.title("Gambar Negatif")
plt.axis("off")

plt.subplot(2,2,3)
plt.plot(hist_r, color = "red", label = "Histogram R awal" )
plt.title("Histogram Gambar Asli")
plt.xlim([0,256])
plt.legend()
plt.subplot(2,2,3)
plt.plot(hist_r, color = "blue", label = "Histogram R awal" )
plt.legend()
plt.subplot(2,2,3)
plt.plot(hist_r, color = "green", label = "Histogram R awal" )
plt.legend()

plt.subplot(2,2,4)
plt.plot(hist_r_neg, color = "blue", label = "Histogram R awal" )
plt.title("Histogram Gambar Negatif")
plt.xlim([0,256])
plt.legend()
plt.subplot(2,2,4)
plt.plot(hist_r_neg, color = "green", label = "Histogram R awal" )
plt.legend()
plt.subplot(2,2,4)
plt.plot(hist_r_neg, color = "red", label = "Histogram R awal" )
plt.legend()
plt.show()

img.imwrite("C:\\Users\\KOMPUTER JARKOM 28\\Documents\\PCD\\negatif poto\\neg.png",image_neg)

