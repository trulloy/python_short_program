#convert image into black and white

from PIL import Image
import sys

input_image = Image.open("public/horse.jpg")
width, height = input_image.size
pixel_map = input_image.load()
maxPixelCount = width * height

print('\033[?25l', end="")
for y in range(0, height-1):
    for x in range(0, width-1):
        r, g, b = input_image.getpixel((x, y))
        avg_value = int((r + g + b) / 3)
        pixel_map[x, y] = (0, 0, 0)
        if avg_value >= 128:
            pixel_map[x, y] = (255, 255, 255)
        
    percent = (y * 100) / (height - 1)
    print(f"Percentage = {int(percent)}%", end='\r')
    sys.stdout.flush()

tempimg = input_image.convert('RGB')
tempimg.save('output/result_horse.jpg')
input_image.close()
tempimg.close()

#convert image into black and white 