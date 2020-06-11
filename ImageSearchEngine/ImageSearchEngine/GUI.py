from PySide2 import QtWidgets,QtGui, QtCore
#from PyQt4 import QtWidgets,QtGui, QtCore
import sys
import ImageFinder
import pathlib

def pathResolver(path):
    newpath = ""
    characters = ()
    for i in range(len(path)):
        if (path[i] == "/" and i != 0):
            characters.append("//")
        else:
            characters.append(path[i])
    return newpath.join(characters)
class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")
        self.setGeometry(300,300,600,700)
        
        self.menu()
        self.searchImagesButton()
        self.numberSelector()
        self.show()
        
    def searchImagesButton(self):
        self.btn = QtWidgets.QPushButton("Search Online",self)
        self.btn.resize(self.btn.minimumSizeHint())
        self.btn.move(100,150)
        self.btn.clicked.connect(self.searchOnline)

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
        self.imageDisplay()

    def numberSelector(self):
        self.numberSelectorBox = QtWidgets.QLineEdit(self)
        self.numberSelectorBox.setMaxLength(3)
        self.numberSelectorBox.setText("5")
        self.numberSelectorBox.move(400,600)
        validator = QtGui.QIntValidator()
        self.numberSelectorBox.setValidator(validator)
        self.numberSelectorBox.textEdited.connect(self.assignnum)

    def imageDisplay(self):
        pixmap = QtGui.QPixmap(fileName = str(pathlib.Path(self.filepath)))
        pixmap = pixmap.scaled(200,200,QtCore.Qt.KeepAspectRatio)
        displayimage = QtWidgets.QLabel()
        displayimage.setPixmap(pixmap)
        displayimage.resize(200,200)
        self.setCentralWidget(displayimage)

    def searchOnline(self):
        ImageFinder.ImageFinder(self.filepath,"Sea", num = self.num)
    
    def assignnum(self):
        self.num = int(self.numberSelectorBox.text())
        print(self.num)

    def exit(self):
        sys.exit()


