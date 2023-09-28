from PIL import Image
from ImagePoint import ImagePoint
import time
from pathlib import Path
import shutil
import os
from PIL.PngImagePlugin import PngInfo

image = Image.open('public/testImg500px.png')
width, height = image.size
print("Image size: ", height, " x ", width, " px")
size_of_squre = 10
list = []

for y in range(0, height, size_of_squre):
    for x in range(0, width, size_of_squre):
         xSize = x + size_of_squre
         ySize = y + size_of_squre
         if width > xSize and height > ySize:
            img = ImagePoint(x, y, xSize, ySize)
            if not img.isSingleColor(image):
                 list.append(img)
    
dirpath = Path('output')
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

isExist = os.path.exists(dirpath)
if not isExist:           
    os.makedirs(dirpath)
    print("output folder created")

a = 1
for obj in list:
    cropImage = image.crop(obj.getBox())
    rgb_im = cropImage.convert('RGB')
    rgb_im.save("output/img_" + str(a) + '.jpg')
    cropImage.close()
    a = a + 1


image.close()