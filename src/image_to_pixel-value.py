from PIL import Image
import numpy as np
import os

img = Image.open('src/Images/sample.png').convert("RGB")
img = np.array(img)

path = 'src/Images/sample.png'
getname = os.path.basename(path)

print(getname)

print(img.shape)

with open('src/store/PixelValue.txt', 'w') as file:

    height, width, channels = img.shape

    for i in range(height):
        for j in range(width):
            pixel = img[i][j]
            file.write(f"Pixels {i}, {j} = {pixel} \n")


