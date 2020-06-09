from PySide2 import QtGui, QtCore
import sys

class GUI(QtGui.QtMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")
        self.setGeometry(300,300,600,700)
        
        #self.menu()
        self.searchImagesOnline()
        self.show()
        
    def searchImagesOnline(self):
        self.btn = QtGui.QPushButton("Search Online", self)
        self.btn.resize(self.btn.minimumSizeHint())
        self.btn.move(60,60)
        self.btn.clicked.connect(self.exit())

    #def menu(self):
    #    browse_option = QtWidgets.QAction("&Browse...", self)
    #    browse_option.setShortcut("Ctrl+N")
    #    browse_option.setToolTip("Browse to your desired file")
    #    #browse_option.triggered.connect(self.exit())
    #    
    #    exit_option = QtWidgets.QAction("&Exit", self)
    #    exit_option.setShortcut("Ctrl+E")
    #    exit_option.setToolTip("Exit the software")
    #    #exit_option.triggered.connect(exit())
    #
    #    self.statusBar()
    #
    #    mainMenu = self.menuBar()
    #    fileMenu = mainMenu.addMenu('&File')
    #    fileMenu.addAction(browse_option)
    #    fileMenu.addAction(exit_option)

    def exit(self):
        print("Exiting")
        sys.exit()


