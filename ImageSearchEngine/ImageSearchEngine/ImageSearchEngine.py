from ImageContainer import *
from ImageFinder import *
import os

#a =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\2.jpg", main = True)
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\1.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\3.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\97.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\4.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\5.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\96.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\6.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\99.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\7.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\98.jpg")
#b =ImageContainer("F:\\Usama\\Projects\\Programming\\ImageSearchEngine\\Picture Set\\2.jpg")

ImageFinder('C:\\Downloads\\2010671.jpg', 'Mountain', 5)

#os.mkdir(r'Image Database\Sea')
#for path in pathlib.Path('Image Database\\Sea\\').iterdir():
#    print(path)
#for count in range(10):
#   print(str('A'+0 for x in range(count)))

#height = 1366
#width = 768
#center = np.zeros((height, width, 1), np.uint8)
#topleft = np.zeros((height, width, 1), np.uint8)
#center = cv2.ellipse(center, (width//2,height//2),(int(0.375*width),int(0.375*height)),0.0,0.0,360.0,(255,255,255),-1)
#topleft = cv2.rectangle(topleft, (0,0),(width//2,height//2),(255,255,255),-1)
#topleft = cv2.subtract(topleft, center)
#cv2.imshow('topleft',topleft)
#cv2.waitKey(0)
#cv2.imshow('center',center)
#cv2.waitKey(0)