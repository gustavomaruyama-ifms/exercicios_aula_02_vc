from skimage import io
import numpy as np
import time

img = io.imread('lenna-master.jpg')
w, h, nc = img.shape

img_float = img.copy().astype(np.float64)

start = time.time()
#Obtendo os canais RGB
red_c = img_float[:,:,0]
green_c = img_float[:,:,1]
blue_c = img_float[:,:,2]

#Obtendo min entre os 3 canais
minimum = np.minimum(red_c,green_c)
minimum = np.minimum(minimum,blue_c)

#Obtendo max entre os 3 canais
maximum = np.maximum(red_c,green_c)
maximum = np.maximum(maximum,blue_c)

#Criando a nova imagem
new_image = np.zeros((w,h), dtype=np.uint8)
new_image = (minimum+maximum)/2

new_image = new_image.astype(np.uint8)
end = time.time()
print('tempo usado: %.3f s'% (end-start))

io.imshow(new_image)
io.show()

