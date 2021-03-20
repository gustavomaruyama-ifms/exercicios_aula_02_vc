from skimage import io
import numpy as np

img = io.imread('lenna-master.jpg')

w, h, nc = img.shape

new_image = np.zeros((w,h), dtype= np.uint8)

for x in range(w):
    for y in range(h):
        red_c = int(img[x,y,0])
        green_c = int(img[x,y,2])
        blue_c = int(img[x,y,1])
        new_image[w,y] = (max(red_c, blue_c, green_c) + min (red_c, blue_c, green_c))/2

io.imsave('lenna-brightness.jpg', new_image)
