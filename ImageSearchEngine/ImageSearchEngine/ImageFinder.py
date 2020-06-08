from icrawler.builtin import BingImageCrawler
from ImageContainer import *
import pathlib
import os
import sys

class ImageFinder:
    def __init__(self, sourcePath, keyword, num, sorting):
        self.sourcePath = sourcePath
        self.keyword = keyword
        self.sorting = sorting
        bingcrawler = BingImageCrawler(storage={'root_dir':'Image Database\\'+self.keyword+'\\'})
        bingcrawler.crawl(keyword=self.keyword,max_num = num)
        self.Sorter()

    def Sorter(self):
        ImageContainer(self.sourcePath, main = True, sorting = self.sorting)
        SimilarityIndex = []
        OrignalFileNumber = []
        count = 0
        for path in pathlib.Path('Image Database\\'+self.keyword+'\\').iterdir():
            tempImageContainer = ImageContainer(str(path))
            SimilarityIndex.append(tempImageContainer.Comparator())
            OrignalFileNumber.append(count+1)
            count += 1
        g = open("Image Database\\Similarity Indices Orignal.txt", "w")
        for i in range(count):
                stringFile = "File Number: "+ str(OrignalFileNumber[i])+ "  Similarity Index: "+ str(SimilarityIndex[i])
                g.write(stringFile)
        g.close()
        SimilarityIndex.append(-1)
        OrignalFileNumber.append(-1)
        k = 0
        for n in range(count):
            for i in range(count-k):
                if(SimilarityIndex[i] > SimilarityIndex[i+1]):
                    SimilarityIndex[-1] = SimilarityIndex[i]
                    SimilarityIndex[i] = SimilarityIndex[i+1]
                    SimilarityIndex[i+1] = SimilarityIndex[-1]
                    OrignalFileNumber[-1] = OrignalFileNumber[i]
                    OrignalFileNumber[i] = OrignalFileNumber[i+1]
                    OrignalFileNumber[i+1] = OrignalFileNumber[-1]
            k += 1

            f = open("Image Database\\Similarity Indices.txt", "w")
            for i in range(count):
                stringFile = "File Number: "+ str(OrignalFileNumber[i])+ "  Similarity Index: "+ str(SimilarityIndex[i])
                f.write(stringFile)
            f.close()

        for count in range(k):
            if(OrignalFileNumber[count]/10 < 1):
                os.rename('Image Database\\'+self.keyword+'\\00000'+str(OrignalFileNumber[count])+'.jpg','Image Database\\'+self.keyword+'\\Sorted_00000'+str(count+1)+'.jpg')
            elif(OrignalFileNumber[count]/100 < 1):
                os.rename('Image Database\\'+self.keyword+'\\0000'+str(OrignalFileNumber[count])+'.jpg','Image Database\\'+self.keyword+'\\Sorted_00000'+str(count+1)+'.jpg')
            elif(OrignalFileNumber[count]/1000 < 1):
                os.rename('Image Database\\'+self.keyword+'\\000'+str(OrignalFileNumber[count])+'.jpg','Image Database\\'+self.keyword+'\\Sorted_00000'+str(count+1)+'.jpg')
            elif(OrignalFileNumber[count]/10000 < 1):
                os.rename('Image Database\\'+self.keyword+'\\00'+str(OrignalFileNumber[count])+'.jpg','Image Database\\'+self.keyword+'\\Sorted_00000'+str(count+1)+'.jpg')
            elif(OrignalFileNumber[count]/100000 < 1):
                os.rename('Image Database\\'+self.keyword+'\\0'+str(OrignalFileNumber[count])+'.jpg','Image Database\\'+self.keyword+'\\Sorted_00000'+str(count+1)+'.jpg')

            #f = open("Image Database\\Similarity Indices Modified.txt", "w")
            #for count in range(k):
            #    f.write("File Number: ", OrignalFileNumber[count], "  Similarity Index: ", SimilarityIndex[count])