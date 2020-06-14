from PySide2 import QtWidgets,QtGui, QtCore
import sys
import ImageFinder
import pathlib
import ctypes

WINDOW_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)*0.75
WINDOW_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)*0.75

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

        self.setWindowTitle("Image Search Engine")
        self.setWindowIcon(QtGui.QIcon(r"Resources\Icons\Main Window.png"))
        self.setGeometry(WINDOW_WIDTH/6,WINDOW_HEIGHT/6,WINDOW_WIDTH,WINDOW_HEIGHT)

        self.setMainImage()
        self.searchImagesButton()
        self.numberSelector()
        self.tagSelector()
        self.destpath()
        self.help()
        self.hSlider()
        self.sSlider()
        self.vSlider()
        self.textWriter()
        self.show()

    def setMainImage(self):
        self.mainImageButton = QtWidgets.QPushButton("Set Source File",self)
        self.mainImageButton.resize(self.mainImageButton.minimumSizeHint())
        self.mainImageButton.move(13*WINDOW_WIDTH/16,5*WINDOW_HEIGHT/8)
        self.mainImageButton.clicked.connect(self.browsewindow)

    def destpath(self):
        self.destpathButton = QtWidgets.QPushButton("Set Destination Path",self)
        self.destpathButton.resize(self.destpathButton.minimumSizeHint())
        self.destpathButton.move(13*WINDOW_WIDTH/16,5.5*WINDOW_HEIGHT/8)
        self.destpathButton.clicked.connect(self.dest)

    def searchImagesButton(self):
        self.btn = QtWidgets.QPushButton("Search Online",self)
        self.btn.resize(self.btn.minimumSizeHint())
        self.btn.move(13*WINDOW_WIDTH/16,6*WINDOW_HEIGHT/8)
        self.btn.clicked.connect(self.searchOnline)

    def help(self):
        self.helpButton = QtWidgets.QPushButton("Help",self)
        self.helpButton.resize(self.helpButton.minimumSizeHint())
        self.helpButton.move(13*WINDOW_WIDTH/16,6.5*WINDOW_HEIGHT/8)
        self.helpButton.clicked.connect(self.helpWindow)

    def okButton(self):
        self.okButton = QtWidgets.QPushButton("OK",self.help)
        self.okButton.resize(self.okButton.minimumSizeHint())
        self.okButton.move(300,240)
        self.okButton.clicked.connect(self.help.close)

    def browsewindow(self):
        self.filepath = QtWidgets.QFileDialog.getOpenFileName(self, "Browse Image File","C:\\","Images (*.png *.jpg *.jpeg *.bmp)")[0]
        print(self.filepath)
        self.filepath = pathResolver(str(self.filepath))
        self.imageDisplay()

    def numberSelector(self):
        self.numberSelectorBox = QtWidgets.QLineEdit(self)
        self.numberSelectorBox.setMaxLength(3)
        self.numberSelectorBox.resize(self.numberSelectorBox.minimumSizeHint())
        self.numberSelectorBox.setText("")
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
        displayimage = QtWidgets.QLabel(self)
        displayimage.setPixmap(pixmap)
        displayimage.setGeometry(QtCore.QRect(0,0,12*WINDOW_WIDTH/16,WINDOW_HEIGHT))
        displayimage.show()

    def textWriter(self):
        boldFont= QtGui.QFont()
        boldFont.setBold(True)
        textNum = QtWidgets.QLabel("Number",self)
        textNum.move(13*WINDOW_WIDTH/16,2*WINDOW_HEIGHT/32)
        textNum.setFont(boldFont)
        textTag = QtWidgets.QLabel("Image Tag",self)
        textTag.move(13*WINDOW_WIDTH/16,4*WINDOW_HEIGHT/32)
        textTag.setFont(boldFont)
        textHSlider = QtWidgets.QLabel("H Bins",self)
        textHSlider.move(13*WINDOW_WIDTH/16,3*WINDOW_HEIGHT/16)
        textHSlider.setFont(boldFont)
        textHSliderMin = QtWidgets.QLabel("0",self)
        textHSliderMin.move(13*WINDOW_WIDTH/16,4.5*WINDOW_HEIGHT/16)
        textHSliderMax = QtWidgets.QLabel("180",self)
        textHSliderMax.move(14.5*WINDOW_WIDTH/16,4.5*WINDOW_HEIGHT/16)
        textSSlider = QtWidgets.QLabel("S Bins",self)
        textSSlider.move(13*WINDOW_WIDTH/16,5*WINDOW_HEIGHT/16)
        textSSlider.setFont(boldFont)
        textSSliderMin = QtWidgets.QLabel("0",self)
        textSSliderMin.move(13*WINDOW_WIDTH/16,6.5*WINDOW_HEIGHT/16)
        textSSliderMax = QtWidgets.QLabel("256",self)
        textSSliderMax.move(14.5*WINDOW_WIDTH/16,6.5*WINDOW_HEIGHT/16)
        textVSlider = QtWidgets.QLabel("V Bins",self)
        textVSlider.move(13*WINDOW_WIDTH/16,7*WINDOW_HEIGHT/16)
        textVSlider.setFont(boldFont)
        textVSliderMin = QtWidgets.QLabel("0",self)
        textVSliderMin.move(13*WINDOW_WIDTH/16,8.5*WINDOW_HEIGHT/16)
        textVSliderMax = QtWidgets.QLabel("256",self)
        textVSliderMax.move(14.5*WINDOW_WIDTH/16,8.5*WINDOW_HEIGHT/16)


    def helpText(self):
        text = QtWidgets.QLabel("""\n                                    Press \"Set Source File\" to select the file for which match has to be found.\n
                                    Press \"Set Destination Path\" to select the folder in which matched images will be stored.\n
                                    Press \"Search Online\" to start finding matches for the sourcce image.\n
                                    Enter \"Number\" to select the number of matching images desired.\n
                                    Enter \"Image Tag\" to give a related keyword to the image.\n
                                    H, S and V bins can also be selected. The recommended values for these are 8, 12 and 3 respectively. 
                                    Deviating too much from these will eihter result in over fitting or underfitting.
                                    If no destination is selected, python working director will be used to store the images. If no number is selected, the
                                    program will use 5 as the desired number of images.
                                    Matches found may not resemble the source image due to the fact that matching is achieved by comparing color histograms
                                    which is sometimes inaccurate.
                                    """
                                    ,self.help)
        text.resize(800,300)
        text.setWordWrap(True)
        text.move(-75,-30)

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

    def hSlider(self):
        self.hslider = QtWidgets.QSlider(self)
        self.hslider.setOrientation(QtCore.Qt.Horizontal)
        self.hslider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.hslider.setTickInterval(1)
        self.hslider.setMaximum(180)
        self.hslider.setMinimum(1)
        self.hslider.resize(1.5*WINDOW_WIDTH/16,WINDOW_HEIGHT/32)
        self.hslider.move(13*WINDOW_WIDTH/16,4*WINDOW_HEIGHT/16)
        self.hValueLabel = QtWidgets.QLabel("1",self)
        self.hValueLabel.move(13.5*WINDOW_WIDTH/16,3.5*WINDOW_HEIGHT/16)
        self.hslider.setValue(8)
        self.assignHValue()
        self.hslider.valueChanged.connect(self.assignHValue)

    def sSlider(self):
        self.sslider = QtWidgets.QSlider(self)
        self.sslider.setOrientation(QtCore.Qt.Horizontal)
        self.sslider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sslider.setTickInterval(1)
        self.sslider.setMaximum(256)
        self.sslider.setMinimum(1)
        self.sslider.resize(1.5*WINDOW_WIDTH/16,WINDOW_HEIGHT/32)
        self.sslider.move(13*WINDOW_WIDTH/16,6*WINDOW_HEIGHT/16)
        self.sValueLabel = QtWidgets.QLabel("1",self)
        self.sValueLabel.move(13.5*WINDOW_WIDTH/16,5.5*WINDOW_HEIGHT/16)
        self.sslider.setValue(12)
        self.assignSValue()
        self.sslider.valueChanged.connect(self.assignSValue)

    def vSlider(self):
        self.vslider = QtWidgets.QSlider(self)
        self.vslider.setOrientation(QtCore.Qt.Horizontal)
        self.vslider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vslider.setTickInterval(1)
        self.vslider.setMaximum(256)
        self.vslider.setMinimum(1)
        self.vslider.resize(1.5*WINDOW_WIDTH/16,WINDOW_HEIGHT/32)
        self.vslider.move(13*WINDOW_WIDTH/16,8*WINDOW_HEIGHT/16)
        self.vValueLabel = QtWidgets.QLabel("1",self)
        self.vValueLabel.move(13.5*WINDOW_WIDTH/16,7.5*WINDOW_HEIGHT/16)
        self.vslider.setValue(3)
        self.assignVValue()
        self.vslider.valueChanged.connect(self.assignVValue)

    def searchOnline(self):
        ImageFinder.ImageFinder(self.filepath, self.tag, self.hNumber, self.sNumber, self.vNumber, self.destpath, self.num)
    
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

    def assignHValue(self):
        self.hNumber = int(self.hslider.value())
        self.hValueLabel.setText(str(self.hNumber))

    def assignSValue(self):
        self.sNumber = int(self.sslider.value())
        self.sValueLabel.setText(str(self.sNumber))

    def assignVValue(self):
        self.vNumber = int(self.vslider.value())
        self.vValueLabel.setText(str(self.vNumber))

    def helpWindow(self):
        self.help = QtWidgets.QWidget()
        self.help.setWindowTitle("Help")
        self.help.setWindowIcon(QtGui.QIcon(r"Resources\Icons\Help.png"))
        self.help.setGeometry(1*WINDOW_WIDTH/3,1*WINDOW_HEIGHT/3,700,280)
        self.helpText()
        self.okButton()
        self.help.show()

    def exit(self):
        sys.exit()
        
        