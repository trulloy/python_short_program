#############################################################
#############################################################     
##                                                         ##
## Reserved by © Trulloy IT (trulloy.com)                  ##
## 1) Developer : Amit Kumar Giri (allyamit@gmail.com)     ##
## 2) Developer : Het Olakiya                              ##
##                                                         ##
##  Since: 25 Sept 2023                                    ##
#############################################################
#############################################################

from PIL import Image
from CreateBorderImage import CreateBorderImage

image = Image.open('public/testImg500px.png')
brImg = CreateBorderImage(image, 10)
brImg.process()

# image = Image.open('public/testCircleImg500px.png')
# brImg = CreateBorderImage(image, 10)
# brImg.process()
