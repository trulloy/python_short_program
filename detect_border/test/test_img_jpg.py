from PIL import Image


im = Image.open("output/img_1")

rgb_im = im.convert('RGB')
rgb_im.save('hourglass_new.jpg')
print("Image saved successfully ...")

im.close()