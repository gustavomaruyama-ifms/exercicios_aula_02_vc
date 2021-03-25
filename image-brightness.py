from skimage import io
import numpy as np
import time

img = io.imread('lenna-master.jpg')

w, h, nc = img.shape

new_image = np.zeros((w,h), dtype= np.uint8)

start = time.time()
for x in range(w):
    for y in range(h):
        red_c = int(img[x,y,0])
        green_c = int(img[x,y,2])
        blue_c = int(img[x,y,1])
        new_image[x,y] = (max(red_c, blue_c, green_c) + min (red_c, blue_c, green_c))/2
end = time.time()
print('tempo usado: %.3f s'% (end-start))


io.imsave('lenna-brightness.jpg', new_image)
