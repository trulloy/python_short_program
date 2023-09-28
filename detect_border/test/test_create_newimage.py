# Imports PIL module
import PIL
from PIL import Image

# creating a image object (new image object) with
# RGB mode and size 200x200
im = PIL.Image.new(mode="RGB", size=(500, 500),color = (255, 255, 255))
rgb_im = im.convert('RGB')
rgb_im.save('testImg.jpg')

# Import an image from directory:
input_image = Image.open("testImg.jpg")
  
# Extracting pixel map:
pixel_map = input_image.load()
  
# Extracting the width and height 
# of the image:
width, height = input_image.size
  
# taking half of the width:
for i in range(width):
    for j in range(height):
        # getting the RGB pixel value.
        r, g, b = input_image.getpixel((i, j))
        # Apply formula of grayscale:
        grayscale = (0.299*r + 0.587*g + 0.114*b)
        # setting the pixel value.
        pixel_map[i, j] = (0, 0, 0)

rgb_im = input_image.convert('RGB')
rgb_im.save("grayscale.jpg")
