from PySide2 import QtWidgets,QtGui, QtCore
#from PyQt4 import QtWidgets,QtGui, QtCore
import sys
import ImageFinder
import pathlib
import ctypes

WINDOW_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)*0.75
WINDOW_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)*0.75
RATIO = WINDOW_WIDTH/WINDOW_HEIGHT

def pathResolver(path):
    newpath = ""
    characters = []
    for i in range(len(path)):
        if (path[i] == "/" and i != 0):
            characters.append("\\\\")
        else:
            characters.append(path[i])
    characters = tuple(characters)
    return newpath.join(characters)


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")
        self.setGeometry(WINDOW_WIDTH/6,WINDOW_HEIGHT/6,WINDOW_WIDTH,WINDOW_HEIGHT)
        
        #self.menu()
        self.searchImagesButton()
        self.numberSelector()
        self.tagSelector()
        self.destpath()
        self.textWriter()
        self.setMainImage()
        self.show()
        
    def searchImagesButton(self):
        self.btn = QtWidgets.QPushButton("Search Online",self)
        self.btn.resize(self.btn.minimumSizeHint())
        self.btn.move(14*WINDOW_WIDTH/16,5*WINDOW_HEIGHT/8)
        self.btn.clicked.connect(self.searchOnline)

    def destpath(self):
        self.destpathButton = QtWidgets.QPushButton("Select Destination",self)
        self.destpathButton.resize(self.destpathButton.minimumSizeHint())
        self.destpathButton.move(13*WINDOW_WIDTH/16,6*WINDOW_HEIGHT/8)
        self.destpathButton.clicked.connect(self.dest)

    def setMainImage(self):
        self.mainImageButton = QtWidgets.QPushButton("Set Man File",self)
        self.mainImageButton.resize(self.mainImageButton.minimumSizeHint())
        self.mainImageButton.move(13*WINDOW_WIDTH/16,5*WINDOW_HEIGHT/8)
        self.mainImageButton.clicked.connect(self.browsewindow)

    def menu(self):
        browse_option = QtWidgets.QAction("&Browse...", self)
        browse_option.setShortcut("Ctrl+N")
        browse_option.setToolTip("Browse to your desired file")
        browse_option.triggered.connect(self.browsewindow)
        
        exit_option = QtWidgets.QAction("&Exit", self)
        exit_option.setShortcut("Ctrl+E")
        exit_option.setToolTip("Exit the software")
        exit_option.triggered.connect(self.exit)
    
        self.statusBar()
    
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(browse_option)
        fileMenu.addAction(exit_option)

    def browsewindow(self):
        self.filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Browse Image File","\\home\\","Images (*.png *.jpg *.jpeg *.bmp)")[0]
        print(self.filepath)
        self.filepath = pathResolver(str(self.filepath))
        print(self.filepath)
        #self.imageDisplay()

    def numberSelector(self):
        self.numberSelectorBox = QtWidgets.QLineEdit(self)
        self.numberSelectorBox.setMaxLength(3)
        self.numberSelectorBox.resize(self.numberSelectorBox.minimumSizeHint())
        self.numberSelectorBox.setText("5")
        self.numberSelectorBox.move(13*WINDOW_WIDTH/16,1.5*WINDOW_HEIGHT/16)
        validator = QtGui.QIntValidator()
        self.numberSelectorBox.setValidator(validator)
        self.numberSelectorBox.textEdited.connect(self.assignNum)

    def tagSelector(self):
        self.tagSelectorBox = QtWidgets.QLineEdit(self)
        self.tagSelectorBox.setMaxLength(100)
        self.tagSelectorBox.resize( self.tagSelectorBox.minimumSizeHint())
        self.tagSelectorBox.setFixedWidth(150)
        self.tagSelectorBox.setText("")
        self.tagSelectorBox.move(13*WINDOW_WIDTH/16,2.5*WINDOW_HEIGHT/16)
        self.tagSelectorBox.textEdited.connect(self.assignTag)

    def imageDisplay(self):
        pixmap = QtGui.QPixmap(self.filepath)
        pixmap = pixmap.scaledToWidth(12*WINDOW_WIDTH/16)
        displayimage = QtWidgets.QLabel(parent = self)
        displayimage.setPixmap(pixmap)
        self.setCentralWidget(displayimage)

    def textWriter(self):
        textNum = QtWidgets.QLabel("Num",self)
        textNum.move(13*WINDOW_WIDTH/16,2*WINDOW_HEIGHT/32)
        textTag = QtWidgets.QLabel("Tag",self)
        textTag.move(13*WINDOW_WIDTH/16,4*WINDOW_HEIGHT/32)

    def paintEvent(self, e):
        painter = QtGui.QPainter()
        painter.begin(self)
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)

        brush.setColor(QtGui.QColor(190,190,190))
        painter.setBrush(brush)
        painter.drawRect(0, 0, 12*WINDOW_WIDTH/16,WINDOW_HEIGHT)
        
        brush.setColor(QtGui.QColor(235,235,235))
        painter.setBrush(brush)
        painter.drawRect(12.0625*WINDOW_WIDTH/16,0,3.9375*WINDOW_WIDTH/16,WINDOW_HEIGHT)

        brush.setStyle(QtCore.Qt.Dense5Pattern)
        brush.setColor(QtGui.QColor(255,255,255))
        painter.setBrush(brush)
        painter.drawRect(12*WINDOW_WIDTH/16,0,WINDOW_WIDTH/256,WINDOW_HEIGHT)

        painter.end()

    def searchOnline(self):
        ImageFinder.ImageFinder(self.filepath, self.tag, self.destpath, self.num)
    
    def dest(self): 
        self.destpath = QtWidgets.QFileDialog.getExistingDirectory(self, "Select desired destination folder","\\home\\", QtWidgets.QFileDialog.ShowDirsOnly )
        print(self.destpath)
        self.destpath = pathResolver(str(self.destpath))
        print(self.destpath)

    def assignNum(self):
        self.num = int(self.numberSelectorBox.text())
        print(self.num)

    def assignTag(self):
        self.tag = str(self.tagSelectorBox.text())

    def exit(self):
        sys.exit()


