
from PIL import Image
from ImagePoint import ImagePoint

class CreateBorderImage:
     
    realImage: Image
    borderImage: Image
    processImage: Image
    pixel_map = None
    sizeOfPixel = 10
    list = []
    
    def __init__(self, real, pixelSize) -> None:
        self.realImage = real
        self.sizeOfPixel = pixelSize
        width, height = real.size
        self.borderImage = Image.new(mode="RGB", size=(width, height),color = (255, 255, 255))
        tempImg = self.borderImage.convert('RGB')
        tempImg.save('tempImg.jpg')
        self.processImage = Image.open("tempImg.jpg")
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
                        self.list.append(img)
        
    def __del__(self):
        self.realImage.close()
        self.borderImage.close()
        self.processImage.close()
    