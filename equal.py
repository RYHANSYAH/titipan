import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def equal(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_normal = (cdf/cdf.max()) * 255
    img_equal = np.interp(image.flatten(),bins[:-1],cdf_normal)
    return img_equal.reshape(image.shape).astype(np.uint8)

path = "C:\\Users\\KOMPUTER JARKOM 32\\Downloads\\p.jpeg"
image = img.imread(path)
imgE = equal(image)
hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
histe, bins= np.histogram(imgE.flatten(), bins=256, range=[0, 256])

plt.figure(figsize=(15,15))

plt.subplot(2,2,1)
plt.imshow(image)
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(imgE)
plt.axis("off")

plt.subplot(2,2,3)
plt.plot(hist)

plt.subplot(2,2,4)
plt.plot(histe)


plt.show()
