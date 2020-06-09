from ImageContainer import *
from ImageFinder import *
import os
from GUI import *
from PySide2.QtWidgets import QApplication


app = QApplication(sys.argv)
window = GUI()
sys.exit(app.exec_())



#ImageFinder('C:\\Downloads\\2010671.jpg', 'Mountain', 5)
