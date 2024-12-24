from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import pyqtSignal, QSize
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QHBoxLayout, QLabel, QVBoxLayout

from .QCircleimage import QCircleimage
from .QBorderButton import QBorderButton

class __Struct:
    def __int__(self, name:str=None, avatar:str=None, ipv4:str=None, ipv6:str=None):
        self.__name = name
        self.__avatar = avatar
        self.__ipv4 = ipv4
        self.__ipv6 = ipv6

class CustomQListWidgetItem(QListWidgetItem):
    def __init__(self, parent, name:str, avatar:str, uuid:str):
        super().__init__(parent=parent)
        self.__avatar = avatar
        self.__name = name
        self.__uuid = uuid

        self.widget = QtWidgets.QWidget()
        self.Hlayout = QHBoxLayout(self.widget)
        self.Vlayout = QVBoxLayout(self.widget)
        self.name_label = QLabel(self.widget)
        self.uuid_label = QLabel(self.widget)
        self.Cimg = QCircleimage(self.widget)

        self.ui_init()

    def ui_init(self):

        self.Hlayout.setSpacing(20)
        self.Hlayout.setContentsMargins(10, 0, 10, 0)  # 移除內邊距

        self.Vlayout.setSpacing(0)
        self.Vlayout.setContentsMargins(0, 10, 0, 10)  # 移除內邊距

        self.setSizeHint(QSize(250, 60))

        self.widget.setObjectName("mainwidget")

        self.Cimg.setFixedSize(55, 55)
        self.Cimg.setimage(self.__avatar)

        font = QtGui.QFont()
        font.setFamily('Arial Black')
        self.name_label.setText(self.__name)
        self.name_label.setObjectName("Name_Lable")
        self.name_label.setStyleSheet("""
        #Name_Lable {
            font-size: 14px;
            color: #1E2022;
        }
        """)
        self.name_label.setFont(font)
        self.uuid_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.uuid_label.setText(f"@{self.__uuid}")
        self.uuid_label.setObjectName("UUID_Lable")
        self.uuid_label.setStyleSheet("""
        #UUID_Lable {
            font-size: 10px;
            color: #52616B;
        }
        """)

        self.Hlayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Hlayout.addWidget(self.Cimg, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Hlayout.addLayout(self.Vlayout)
        self.Vlayout.addWidget(self.name_label, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Vlayout.addWidget(self.uuid_label, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

class QTitlebar(QtWidgets.QWidget):
    titlebar_signal = pyqtSignal(str)

    def __init__(self, parent=None, title: str = None):
        super().__init__(parent=parent)
        self.__title = title
        self.setContentsMargins(0, 0, 0, 0)

        # 設置界面
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.topbarHlay = QtWidgets.QHBoxLayout(self)
        self.titleLable = QtWidgets.QLabel(self)
        self.add_button = QBorderButton(self, name="", sizew=16, sizeh=16)

        self.ui_init()

    def ui_init(self):
        # 設置標題
        self.titleLable.setText(self.__title)
        self.titleLable.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.titleLable.setObjectName("Title_Lable")
        self.titleLable.setStyleSheet("""
        #Title_Lable {
           font-family: Arial Black;
           font-size: 16px;
           color: #1E2022;
        }
        """)

        self.add_button.seticon(iconpath="D:/python/CatChat/res/add.png")

        self.topbarHlay.addWidget(self.titleLable, 1,
                                  alignment=QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignCenter)
        self.topbarHlay.addWidget(self.add_button, 1,
                                  alignment=QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignCenter)

class QListview(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui_init()

    def ui_init(self):
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.setSpacing(2)

        self.setObjectName("ListW")
        self.setStyleSheet("""
        #ListW {
            background-color: transparent;
            border: none;
            outline: 0px;
        }
        QListWidget::item {
            background-color: transparent;
            border: none;
        }
        QListWidget::item:selected {
            background-color: transparent;
            color: inherit;
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
        for i in range(0, 10):
            self.cl = CustomQListWidgetItem(self.__listview, "QAQ", "D:/python/CatChat/res/avatar.jpg", "204104")
            self.__listview.setItemWidget(self.cl, self.cl.widget)

        self.ui_init()

    def ui_init(self):
        self.setMinimumSize(250, 355)
        self.setMaximumSize(250, 359)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)

        self.Vlayout.setSpacing(0)
        self.Vlayout.setContentsMargins(0,0,0,0)

        self.Vlayout.addWidget(self.__topbar, 0, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.Vlayout.addWidget(self.__listview, 1)

    def setmeun_action(self, win):
        self.__topbar.add_button.clicked.connect(win.show)