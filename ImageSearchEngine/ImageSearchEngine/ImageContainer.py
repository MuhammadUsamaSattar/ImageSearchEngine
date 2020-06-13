import cv2
import numpy as np
import math


class ImageContainer:
    bin_main = [[],[],[],[],[]]
    height_main = 0
    width_main = 0

    def __init__ (self, path,hDivisions = 8, sDivisions = 12, vDivisions = 3, main = False,):
        bin_main = [[0 for i in range(hDivisions*sDivisions*vDivisions)]for j in range(5)]
        self.main = main
        self.path = path
        self.hDivisions = hDivisions
        self.sDivisions = sDivisions
        self.vDivisions = vDivisions
        image = cv2.imread(self.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        self.image = image
        print(path)
        self.height, self.width, channel = image.shape
        
        if(self.main == True):
            ImageContainer.height_main, ImageContainer.width_main, _ = image.shape
            self.width = ImageContainer.width_main 
            self.height = ImageContainer.height_main
        elif(self.height > ImageContainer.height_main or self.width > ImageContainer.width_main):
                image = cv2.resize(image, (ImageContainer.width_main, ImageContainer.height_main))
                self.width = ImageContainer.width_main
                self.height = ImageContainer.height_main

        #Following portion divides the image into five parts
        center = np.zeros((self.height, self.width, 3), np.uint8)
        topleft = np.zeros((self.height, self.width, 3), np.uint8)
        topright = np.zeros((self.height, self.width, 3), np.uint8)
        bottomleft = np.zeros((self.height, self.width, 3), np.uint8)
        bottomright = np.zeros((self.height, self.width, 3), np.uint8)

        center = cv2.ellipse(center, (self.width//2,self.height//2),(int(0.375*self.width),int(0.375*self.height)),0.0,0.0,360.0,(255,255,255),-1)
        
        topleft = cv2.rectangle(topleft, (0,0),(self.width//2,self.height//2),(255,255,255),-1)
        topleft = cv2.subtract(topleft, center)
        
        topright = cv2.rectangle(topright, (self.width,0),(self.width//2,self.height//2),(255,255,255),-1)
        topright = cv2.subtract(topright, center)
        
        bottomleft = cv2.rectangle(bottomleft, (0,self.height),(self.width//2,self.height//2),(255,255,255),-1)
        bottomleft = cv2.subtract(bottomleft, center)
        
        bottomright = cv2.rectangle(bottomright, (self.width,self.height),(self.width//2,self.height//2),(255,255,255),-1)
        bottomright = cv2.subtract(bottomright, center)

        center = cv2.bitwise_and(image, center, mask = None)
        topleft = cv2.bitwise_and(image, topleft, mask = None)
        topright = cv2.bitwise_and(image, topright, mask = None)
        bottomleft = cv2.bitwise_and(image, bottomleft, mask = None)
        bottomright = cv2.bitwise_and(image, bottomright, mask = None)

        self.region = [topleft, topright, center, bottomleft, bottomright]

        self.BinSort()

    def BinSort(self):
        self.bin = [[0 for i in range(self.hDivisions * self.sDivisions * self.vDivisions)]for j in range(5)]
        for i in range(5):
            totalpixels = 0
            for x in range(self.width):
                for y in range(self.height):
                    h, s, v = self.region[i][y, x]
                    if (h != 0 and s != 0 and v != 0):
                        totalpixels += 1
                        v = math.ceil(v/(255/self.vDivisions)) -1
                        s = math.ceil(s/(255/self.sDivisions)) -1
                        h = math.ceil(h/(179/self.hDivisions)) -1
                        self.bin[i][self.sDivisions*self.vDivisions*h + s*self.vDivisions + v] += 1  #Places the pixel in a bin according to HSV value
            for n in range(self.hDivisions * self.sDivisions * self.vDivisions):
                self.bin[i][n] /= totalpixels
        if(self.main == True): ImageContainer.bin_main = self.bin
        #cv2.imshow("green", self.region[1]);cv2.waitKey();cv2.destroyAllWindows()

    def Comparator(self):
        if(self.main == False):
            average = 0
            for i in range(5):
                average += self.chiSquare(i)
                #print(self.chiSquare(i))
            average /= 5
            return average
        
    def chiSquare(self,i):
        d = 0.5* np.sum([(a-b)**2 / (a+b+float(1e-10)) for (a,b) in zip(self.bin[i],ImageContainer.bin_main[i])])
        return d
