from PIL import Image

input_image = Image.open("public/testheart500px.png")
width, height = input_image.size
pixel_map = input_image.load()

for y in range(0, height):
    for x in range(0, width):
        r, g, b = input_image.getpixel((x, y))
        avg_value = int((r + g + b) / 3)

        if avg_value >= 128:
            ""
            #pixel_map[x, y] = (255, 255, 255)
        if r > 200 and g > 200 and b < 100:                
            pixel_map[x, y] = (190, 190, 190)
            
        if r > 200 and g < 100 and b < 100:                     
            pixel_map[x, y] = (110, 110, 110)
                
        if r > 200 and g < 100 and b < 100:
            pixel_map[x, y] = (110, 110, 110)
            
input_image.save('output/result_doodle.jpg')
input_image.close()
