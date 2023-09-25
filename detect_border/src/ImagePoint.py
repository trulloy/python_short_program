from PIL import Image

class ImagePoint:
    x1: int = 0
    y1: int = 0
    x2: int = 0
    y2: int = 0
    
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def getBox(self):
        s=(self.x1, self.y1, self.x2, self.y2)
        return s
    
    def isSingleColor(self, image: Image) -> bool:
        flag = True
        self.myformatt()
        previous_color = image.getpixel((self.x1, self.x2))
        for i in range(self.x1, self.x2):
            for j in range(self.y1, self.y2):
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
        print("Point[",self.x1,self.x2,self.y1,self.y2,"]")
        
    @classmethod
    @staticmethod
    def checkException(img:Image, x, y):
        img.getpixel((x, y))