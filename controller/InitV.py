from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import StandardTitleBar

from view import QInitView
from model import *

class InitV(QInitView):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.stackedwidget = StackedWidget()
        self.welcomview = Welcome()
        self.ifsview = InforSetting()

        self.ui_init()

    def ui_init(self):
        self.titleBar.maxBtn.deleteLater()
        self.titleBar._isDoubleClickEnabled = False

        self.stackedwidget.addWidget(self.welcomview)
        self.stackedwidget.addWidget(self.ifsview)
        self.Vlayout.addWidget(self.stackedwidget)

        self.stackedwidget.currentChanged.connect(self.anime_start)

    def anime_start(self, index):
        if index == 1:
            self.ifsview.nameedit.start_animation()
        else:
            self.ifsview.nameedit.end_animation()

class Welcome(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(40)
        self.setFont(font)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("𝓦𝓮𝓵𝓬𝓸𝓶𝓮")

class InforSetting(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vmlayout = QVBoxLayout(self)
        self.vlayout = QVBoxLayout()
        self.circleimage = QCircleimage(self)
        self.nameedit = QLineEditBar(self)
        self.donebut = QBorderButton(self, sizew=30, sizeh=20)

        self.ui_init()

    def ui_init(self):
        self.circleimage.setFixedSize(200, 200)
        self.circleimage.setimage("D:/python/CatChat/res/baseuser.png")

        self.circleimage.clicked.connect(self.imageevent)

        self.nameedit.setFixedHeight(30)
        self.nameedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameedit.setStyleSheet("""
        QLineEdit {
           font-family: Arial Black;
           font-size: 22px;
           background-color: transparent;
           border-radius: 0px;
           padding: 2px;
           border-bottom: 2px solid #A7A7A7;
           color: #4E4E4E;
        }
        """)

        self.donebut.setStyleSheet("""
        #QBorderButton {
            padding: 5px;
            font-size: 14px;
            font-family: Arial Black;
            background-color: #52616B;
            border-radius: 5px;
            color: #F0F5F9;
        }
        """)

        self.donebut.seticon("D:/python/CatChat/res/left-arrow.png")

        self.vlayout.setSpacing(5)
        self.vlayout.addWidget(self.circleimage, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.nameedit, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        self.vlayout.setContentsMargins(0, 60, 0, 60)

        self.vmlayout.addLayout(self.vlayout)
        self.vmlayout.addWidget(self.donebut, 0, alignment=Qt.AlignmentFlag.AlignRight)

    def imageevent(self):
        dialog = QFileDialog()
        dialog.setNameFilter("All images (*.png *.jpg)")
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialogss = dialog.exec()
        if dialogss:
            filePath = dialog.selectedFiles()
            if filePath:
                self.circleimage.setimage(filePath[0])
            else:
                return
        else:
            return