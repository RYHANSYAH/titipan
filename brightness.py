import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def bright(image, factor):
    imgBright = image.astype(np.float32)
    imgBright = imgBright + factor
    imgBright = np.clip(imgBright, 0, 255)
    return imgBright.astype(np.uint8)

def contrast(image, factor):
    mean = 128
    img_contrast = image.astype(np.float32)
    img_contrast = mean + factor * (img_contrast - mean)
    img_contrast = np.clip(img_contrast, 0, 255)
    return img_contrast.astype(np.uint8)

def blend(image1,f1,image2,f2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)

    result = (img1 * f1) + (img2 * f2)
    result = np.clip(result,0,255)
    return result.astype(np.uint8)

path = "C:\\Users\\KOMPUTER JARKOM 32\\Pictures\\coba.jpg"
path2 = "C:\\Users\\KOMPUTER JARKOM 32\\Downloads\\p.jpeg"

image = img.imread(path)
image2 = img.imread(path2)
imgjoin = blend(image,0.3,image2,0.7)

hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

imgContrast = contrast(image, 3)
histC, binsC = np.histogram(imgContrast.flatten(), bins=256, range=[0, 256])

plt.figure(figsize=(9,6))

plt.subplot(3, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(3, 2, 2)
plt.imshow(imgContrast)
plt.title("Gambar Kontras")
plt.axis("off")

plt.subplot(3, 2, 3)
plt.plot(hist, color='blue', label='Histogram Gambar Asli')
plt.title("Histogram Gambar Asli")
plt.xlim([0, 255])
plt.legend()

plt.subplot(3, 2, 4)
plt.plot(histC, color='orange', label='Histogram Gambar Kontras')
plt.title("Histogram Gambar Kontras")
plt.xlim([0, 255])
plt.legend()

plt.subplot(3,2,5)
plt.imshow(imgjoin)

plt.tight_layout()
plt.show()
