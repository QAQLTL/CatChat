from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QAbstractAnimation, QVariantAnimation, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import QListWidget

class __Struct:
    def __int__(self, name:str=None, avatar:str=None, ipv4:str=None, ipv6:str=None):
        self.__name = name
        self.__avatar = avatar
        self.__ipv4 = ipv4
        self.__ipv6 = ipv6

class QTitlebar(QtWidgets.QWidget):
    titlebar_signal = pyqtSignal(str)

    def __init__(self, parent=None, title: str = None):
        super().__init__(parent=parent)
        self.__title = title
        self._angle = [0, 180]  # 初始化角度
        self.iconpixmap = QPixmap("D:/python/CatChat/res/down.png")  # 加載圖片
        self.setContentsMargins(0, 0, 0, 0)

        # 設置動畫
        self.animation = QVariantAnimation(self)

        # 設置界面
        # self.resize(250, 40)
        # self.setMinimumSize(250, 40)
        # self.setMaximumSize(250, 40)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.topbarHlay = QtWidgets.QHBoxLayout(self)
        self.titleLable = QtWidgets.QLabel(self)
        self.iconlable = QtWidgets.QLabel(self)

        self.ui_init()

    def ui_init(self):
        # 設置標題
        self.topbarHlay.addWidget(self.titleLable, alignment=QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily('Arial Black')
        self.titleLable.setText(self.__title)
        self.titleLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.titleLable.setObjectName("Title_Lable")
        self.titleLable.setStyleSheet("""
        #Title_Lable {
           font-size: 15px;
           color: #606060;
        }
        """)
        self.titleLable.setFont(font)

        # 設置 iconlable 大小
        self.iconlable.setFixedSize(15, 15)
        self.iconlable.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.topbarHlay.addWidget(self.iconlable, alignment=QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignCenter)

        # 初始化顯示圖片
        self.update_icon(0)

    def update_icon(self, angle):
        self._angle[0] = angle
        self._angle[1] = angle + 180
        # 根據當前角度旋轉圖片並更新 QLabel 顯示
        trans = QTransform().rotate(angle)
        rotated_pixmap = self.iconpixmap.transformed(trans)
        self.iconlable.setPixmap(rotated_pixmap)
        self.iconlable.setScaledContents(True)

    def mousePressEvent(self, event):
        if self.animation.state() == QAbstractAnimation.State.Running:
            pass
        else:
            self.animation.setDuration(500)  # 設置動畫持續時間
            self.animation.setStartValue(self._angle[0])
            self.animation.setEndValue(self._angle[1])
            self.animation.valueChanged.connect(self.update_icon)  # 每次值改變時更新圖標
            self.animation.start()

class QListview(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumHeight(400)
        self.setObjectName("ListW")

        self.ui_init()

    def ui_init(self):
        self.setStyleSheet("""
        #ListW {
            color: #FFFFFF;
            background-color: #33373B;
        }
        """)

class QFramelessmenu(QtWidgets.QWidget):
    def __init__(self, parent=None, title: str = None):
        super().__init__(parent=parent)
        self.__title = title
        self.__datalist = []

        self.Vlayout = QtWidgets.QVBoxLayout(self)
        self.__topbar = QTitlebar(parent=self, title=self.__title)
        self.__listview = QListview(self)
        self.ui_init()

    def ui_init(self):
        self.resize(250, 300)
        self.setMinimumSize(250, 300)
        self.setMaximumSize(250, 300)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)

        self.Vlayout.setSpacing(0)
        self.Vlayout.setContentsMargins(0,0,0,0)

        self.Vlayout.addWidget(self.__topbar, 0, alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        self.Vlayout.addWidget(self.__listview, 1, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
