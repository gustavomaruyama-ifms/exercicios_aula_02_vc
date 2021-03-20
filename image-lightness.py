from skimage import io
import numpy as np

img = io.imread('lenna-master.jpg')

w, h, nc = img.shape

new_image = np.zeros((w,h), dtype = np.uint8)

for x in range(w):
    for y in range(h):
        red_c = int(img[x,y,0])
        green_c = int(img[x,y,1])
        blue_c = int(img[x,y,2])
        new_image[x,y] = (red_c * 0.21) + (green_c * 0.71) + (blue_c * 0.07)

io.imsave('lenna-lightness.jpg', new_image)        

