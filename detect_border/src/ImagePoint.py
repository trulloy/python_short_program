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
class ImagePoint:
    x1: int = 0
    y1: int = 0
    x2: int = 0
    y2: int = 0
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def getBox(self):
        s=(self.x1, self.y1, self.x2, self.y2)
        return s
    
    def isSingleColor(self, image: Image) -> bool:
        flag = True
        maxX = self.x2 - 1
        maxY = self.y2 - 1
        previous_color = image.getpixel((self.x1, self.y1))
        
        for i in range(self.x1, maxX):
            for j in range(self.y1, maxY):
                current_color = image.getpixel((i,j))
                if (previous_color == current_color):
                    flag = True
                else:
                    flag = False
                    break
                previous_color = current_color
            if (flag == False):
                break
        if (flag):
            return True
        else:
            return False
        
    def myformatt(self):
        return "Point[" + str(self.x1) + ", " + str(self.x2) + ", " + str(self.y1) + ", "  + str(self.y2) + "]"
    
    def printPixelColor(self, image:Image):
        flag = True
        maxX = self.x2 - 1
        maxY = self.y2 - 1
        previous_color = image.getpixel((0, 0))
        
        for i in range(self.x1, maxX):
            for j in range(self.y1, maxY):
                current_color = image.getpixel((i,j))
                print(i,j, " ->", current_color)