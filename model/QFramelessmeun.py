from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QIcon


class __Struct:
    def __int__(self, name:str=None, avatar:str=None, ipv4:str=None, ipv6:str=None):
        self.__name = name
        self.__avatar = avatar
        self.__ipv4 = ipv4
        self.__ipv6 = ipv6

class QFramelessmeun(QtWidgets.QWidget):
    def __init__(self, parent=None, title:str=None):
        super().__init__(parent=parent)
        self.__title = title
        self.__list = []

        self.Vlayout = QtWidgets.QVBoxLayout(self)
        self.__topbar = QtWidgets.QWidget(self)
        self.topbarHlay = QtWidgets.QHBoxLayout(self.__topbar)

        self.titleLable = QtWidgets.QLabel(self.__topbar)
        self.iconlable = QtWidgets.QLabel(self.__topbar)
        self.ui_init()

    def ui_init(self):
        self.resize(250, 250)
        self.setMinimumSize(250, 250)
        self.setMaximumSize(250, 250)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)

        self.__topbar.resize(250, 40)
        self.Vlayout.addWidget(self.__topbar, alignment=QtCore.Qt.AlignmentFlag.AlignTop)

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

        self.iconlable

    def settitleicon(self):
        pass

    def add(self):
        pass

    def getlen(self) -> int:
        return len(self.__list)
