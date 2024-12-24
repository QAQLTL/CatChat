from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import StandardTitleBar

from view import QInitView
from model import StackedWidget, QCircleimage

class InitV(QInitView):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.stackedwidget = StackedWidget()

        self.ui_init()

    def ui_init(self):
        self.titleBar.maxBtn.deleteLater()
        self.titleBar._isDoubleClickEnabled = False

        welcomview = Welcome()
        iis_view = ImageInforSetting()
        self.stackedwidget.addWidget(welcomview)
        self.Vlayout.addWidget(self.stackedwidget)

class Welcome(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(40)
        self.setFont(font)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("𝓦𝓮𝓵𝓬𝓸𝓶𝓮")

class ImageInforSetting(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vlayout = QVBoxLayout(self)
        self.circleimage = QCircleimage(self)

        self.ui_init()

    def ui_init(self):
        self.circleimage.setFixedSize(200, 200)
        self.circleimage.setimage("D:/python/CatChat/res/avatar.jpg")

        self.vlayout.addWidget(self.circleimage, 0, alignment=Qt.AlignmentFlag.AlignCenter)
