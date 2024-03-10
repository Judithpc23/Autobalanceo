
import os
import numpy as np 

from PIL import Image

ejemplo_dir = 'Data/bike'

with os.scandir(ejemplo_dir) as ficheros:
    ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]

print(ficheros)

for img in ficheros:
    im = Image.open(img)
    rgb_im = im.convert('RGB')
    img = img.split('.')[0]
    rgb_im.save(img,'.jpg', quality=95)