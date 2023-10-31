from PySide6 import QtCore
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QFileDialog
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont, PushButton
from qfluentwidgets import FluentIcon as FIF

from .img2ico import func


class HomeWidget(QFrame):

    def __init__(self: str, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("Home-Interface")

        self.select_file_btn = PushButton("Select File", self)
        self.vBoxLayout = QVBoxLayout(self)

        self.select_file_btn.clicked.connect(self.select_file)

        self.vBoxLayout.addWidget(self.select_file_btn, 1, Qt.AlignCenter)
    
    def select_file(self):
        dialog = QFileDialog(self)
        filePath, filterType  = dialog.getOpenFileName(self, 'Open File')
        func(filePath)
    
    @QtCore.Slot()
    def on_finished(self) -> None:
        for path in self.dialog.selectedFiles():
            print(path)



class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = HomeWidget(self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')

    def initWindow(self):
        # self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('Img2ico')

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
