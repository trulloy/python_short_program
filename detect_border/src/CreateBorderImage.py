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
from ImagePoint import ImagePoint
from pathlib import Path
import shutil
import os

class CreateBorderImage:
     
    realImage: Image
    borderImage: Image
    processImage: Image
    pixel_map = None
    sizeOfPixel = 10
    list = []
    
    def __init__(self, real: Image, pixelSize: int) -> None:
        dirpath = Path('output')
        if dirpath.exists() and dirpath.is_dir():
            shutil.rmtree(dirpath)

        isExist = os.path.exists(dirpath)
        if not isExist:           
            os.makedirs(dirpath)
        self.realImage = real
        self.sizeOfPixel = pixelSize
        width, height = real.size
        self.borderImage = Image.new(mode="RGB", size=(width, height),color = (255, 255, 255))
        tempImg = self.borderImage.convert('RGB')
        tempImg.save('output/tempImg.jpg')
        self.processImage = Image.open("output/tempImg.jpg")
        self.pixel_map = self.processImage.load()
        
    def process(self) -> None:
        '''Write the logic here'''
        width, height = self.realImage.size
        for y in range(0, height, self.sizeOfPixel):
            for x in range(0, width, self.sizeOfPixel):
                xSize = x + self.sizeOfPixel
                ySize = y + self.sizeOfPixel
                if width > xSize and height > ySize:
                    img = ImagePoint(x, y, xSize, ySize)
                    if not img.isSingleColor(self.realImage):
                        self.copyPixels(img)

        rgb_im = self.processImage.convert('RGB')
        rgb_im.save("output/borderscale.jpg")
        

        ## Crop only border image
        # a = 1
        # for obj in list:
        #     cropImage = image.crop(obj.getBox())
        #     rgb_im = cropImage.convert('RGB')
        #     rgb_im.save("output/img_" + str(a) + '.jpg')
        #     cropImage.close()
        #     a = a + 1

    def copyPixels(self, box: ImagePoint) -> bool:
        maxX = box.x2 - 1
        maxY = box.y2 - 1
        
        for i in range(box.x1, maxX):
            for j in range(box.y1, maxY):
                r, g, b = self.realImage.getpixel((i, j))
                self.pixel_map[i, j] = (r, g, b)
        
    def __del__(self):
        self.realImage.close()
        self.borderImage.close()
        self.processImage.close()
    