from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QVariantAnimation, pyqtSlot, QVariant, QAbstractAnimation
from PyQt6.QtGui import QIcon, QPixmap, QTransform


class __Struct:
    def __int__(self, name:str=None, avatar:str=None, ipv4:str=None, ipv6:str=None):
        self.__name = name
        self.__avatar = avatar
        self.__ipv4 = ipv4
        self.__ipv6 = ipv6


class QTitlebar(QtWidgets.QWidget):
    def __init__(self, parent=None, title:str=None):
        super().__init__(parent=parent)
        self.__title = title
        self.__angle = [0, 180]

        self.resize(250, 40)
        self.topbarHlay = QtWidgets.QHBoxLayout(self)
        self.titleLable = QtWidgets.QLabel(self)
        self.iconlable = QtWidgets.QLabel(self)
        self.iconpixmap = QPixmap()
        self.ui_init()

    def ui_init(self):
        self.topbarHlay.addWidget(self.titleLable, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
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
        self.iconlable.setFixedSize(15, 15)
        self.iconlable.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.iconpixmap.load("D:/python/CatChat/res/down.png")
        self.iconlable.setPixmap(self.iconpixmap)
        self.iconlable.setScaledContents(True)
        self.topbarHlay.addWidget(self.iconlable, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

    def mousePressEvent(self, a0):
        animation = QVariantAnimation(self.iconlable)
        animation.setDuration(300)
        animation.setStartValue(self.__angle[0])
        animation.setEndValue(self.__angle[1])
        animation.valueChanged.connect(self.angle)
        animation.start()

    @pyqtSlot(QVariant)
    def angle(self, value: float) -> None:
        self.__angle[0] = value
        self.__angle[1] = value+180
        trans = QTransform()
        trans.rotate(value)
        self.iconlable.setPixmap(self.iconpixmap.transformed(trans))

class QFramelessmeun(QtWidgets.QWidget):
    def __init__(self, parent=None, title:str=None):
        super().__init__(parent=parent)
        self.__title = title
        self.__list = []

        self.Vlayout = QtWidgets.QVBoxLayout(self)
        self.__topbar = QTitlebar(parent=self, title=self.__title)
        self.ui_init()

    def ui_init(self):
        self.resize(250, 250)
        self.setMinimumSize(250, 250)
        self.setMaximumSize(250, 250)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)

        self.__topbar.resize(250, 40)
        self.Vlayout.addWidget(self.__topbar, alignment=QtCore.Qt.AlignmentFlag.AlignTop)

    def getlen(self) -> int:
        return len(self.__list)
