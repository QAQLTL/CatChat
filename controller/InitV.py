from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import StandardTitleBar

from view import QInitView
from model import *
from common import *

ip = IPclass()
datacontroller = DataController()

class InitV(QInitView):
    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.stackedwidget = StackedWidget()
        self.welcomview = Welcome()
        self.ifsview = InforSetting()
        self.sslcryptoview = SslCrypto()

        self.settings = Config("Personal")

        self.ui_init()

    def ui_init(self):
        self.titleBar.maxBtn.deleteLater()
        self.titleBar._isDoubleClickEnabled = False

        self.stackedwidget.addWidget(self.welcomview)
        self.stackedwidget.addWidget(self.ifsview)
        self.Vlayout.addWidget(self.stackedwidget)

        self.ifsview.donebut.clicked.connect(self.add_widget)
        self.stackedwidget.currentChanged.connect(self.anime_start)

    def anime_start(self, index):
        if index == 1:
            self.ifsview.nameedit.start_animation()
            self.stackedwidget.removeWidget(self.sslcryptoview)
        else:
            self.ifsview.nameedit.end_animation()

    def add_widget(self):
        if self.ifsview.nameedit.text() and self.ifsview.circleimage.image():
            image_path = datacontroller.file_copy_path(self.ifsview.circleimage.imagepath, "images", "personal_avatar", ".png")
            self.settings.save_avatar_path(image_path)
            self.settings.save_username(self.ifsview.nameedit.text())
            self.settings.save_useripv4(ip.curripv4)
            self.stackedwidget.addWidget(self.sslcryptoview)
            self.stackedwidget.animateToPage(2, "left")

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
        self.bottomlayout = QHBoxLayout()
        self.circleimage = QCircleimage(self)
        self.nameedit = QLineEditBar(self)
        self.donebut = QBorderButton(self, sizew=20, sizeh=20)

        self.ui_init()

    def ui_init(self):
        self.circleimage.setFixedSize(200, 200)

        self.circleimage.clicked.connect(self.imageevent)

        self.nameedit.setFixedWidth(0)
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
        self.bottomlayout.addWidget(self.donebut, 0, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        self.vmlayout.addLayout(self.bottomlayout)

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

class ComputerInfor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hlayout = QHBoxLayout(self)
        self.ipv4group = QGroupBox("IPv4")
        self.ipv6group = QGroupBox("IPv6")

        self.ipv4Lable = QLineLabel(self, ip.curripv4)
        self.ipv4layout = QHBoxLayout()
        self.ipv6Lable = QLineLabel(self, ip.curripv6)
        self.ipv6layout = QHBoxLayout()

        self.ui_init()

    def ui_init(self):
        self.ipv4layout.addWidget(self.ipv4Lable)
        self.ipv6layout.addWidget(self.ipv6Lable)

        self.ipv4Lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ipv4group.setLayout(self.ipv4layout)
        self.ipv6Lable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ipv6group.setLayout(self.ipv6layout)

        self.hlayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout.addWidget(self.ipv4group, alignment=Qt.AlignmentFlag.AlignCenter)
        self.hlayout.addWidget(self.ipv6group, alignment=Qt.AlignmentFlag.AlignCenter)

        self.style()

    def style(self):
        self.ipv4Lable.setFixedHeight(20)
        self.ipv6Lable.setFixedHeight(20)
        self.ipv4Lable.setStyleSheet("""
        QLabel {
           font-family: Arial Black;
           font-size: 20px;
           background-color: transparent;
           border-radius: 0px;
           padding: 0px;
           border-bottom: 2px solid #A7A7A7;
           color: #4E4E4E;
        }
        """)
        self.ipv6Lable.setStyleSheet("""
        QLabel {
           font-family: Arial Black;
           font-size: 20px;
           background-color: transparent;
           border-radius: 0px;
           padding: 0px;
           border-bottom: 2px solid #A7A7A7;
           color: #4E4E4E;
        }
        """)
        self.setStyleSheet("""
        QGroupBox {
            font: bold 10px;
            color: #52616B;
            border: 1px solid #A7A7A7;
            border-radius: 5px;
            margin-top: 5px;
        }
        QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 5px;
        }
        """)

class SslCrypto(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def ui_init(self):
        pass