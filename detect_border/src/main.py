from PIL import Image
from ImagePoint import ImagePoint

image = Image.open('detect_border/public/img.png')
width, height = image.size
print("Image size: ", height, " x ", width, " px")

size_of_squre = 5
list = []

for y in range(0, height-1, size_of_squre):
    for x in range(0, width-1, size_of_squre):
        # img = ImagePoint(x, y, x+size_of_squre, y+size_of_squre)
        # if not img.isSingleColor(image):
        #     list.append(img)
        print("this is y:",y)
        print("this is x",x)
############### Error:- Index out of range ###############
#ImagePoint.checkException(image, 45, 49)        
image.close()


