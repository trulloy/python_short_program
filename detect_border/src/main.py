#############################################################
#############################################################     
##                                                         ##
##  Reserved by © Trulloy IT (trulloy.com)                 ##
##  1) Developer : Amit Kumar Giri (allyamit@gmail.com)    ##
##  2) Developer : Het Olakiya (olakiyahet@gmail.com)      ##
##                                                         ##
##  Since: 25 Sept 2023                                    ##
#############################################################
#############################################################

from PIL import Image
from CreateBorderImage import CreateBorderImage

# image = Image.open('public/result_horse.jpg')
# brImg = CreateBorderImage(image, 10)
# brImg.process()

image = Image.open('public/test_light_circle.png')
brImg = CreateBorderImage(image, 10)
brImg.process(5)

# image = Image.open('public/testheart500px.png')
# brImg = CreateBorderImage(image, 10)
# brImg.process()

# image = Image.open('public/test_design500px.png')
# brImg = CreateBorderImage(image, 10)
# brImg.process()

# image = Image.open('public/test_doodle500px.png')
# brImg = CreateBorderImage(image, 10)
# brImg.process()