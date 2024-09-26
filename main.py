from PyQt6.QtWidgets import *

import sys

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Automation Controller")
        self.setGeometry(50,100,640,680)


def main():
    app = QApplication([])
    window = mainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
