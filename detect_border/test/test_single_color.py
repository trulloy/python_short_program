from PIL import Image
from ImagePoint import ImagePoint

checkImage = ImagePoint(0, 0, 50, 50)
# cropImage = image.crop(checkImage.getBox())
# cropImage.save("output/img_" + str(a),  "PNG")

myImage = Image.open('public/black.png')
width, height = myImage.size
print("Image size: ", height, " x ", width, " px")
print("Is Image having other colors: ")
checkImage.printPixelColor(myImage)
print(checkImage.isSingleColor(myImage))
myImage.close()