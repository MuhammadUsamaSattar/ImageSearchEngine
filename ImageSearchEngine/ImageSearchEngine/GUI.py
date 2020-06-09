from PySide2.QtWidgets import QMainWindow

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello")
        self.setGeometry(300,300,600,700)
        self.show()
        

