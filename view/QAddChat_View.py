from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from qframelesswindow import FramelessWindow

from model.QLineEditBar import QLineEditBar
from model import QBorderButton

class QAddView(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__Vlayout = QVBoxLayout(self)
        self.__Hlayout = QHBoxLayout()
        self.__searchber = QLineEditBar()
        self.__searchbut = QBorderButton()
        self.ui_init()

    def ui_init(self):
        self.setObjectName("AddUi")
        self.setContentsMargins(10, 40, 10, -1)
        self.setFixedSize(400, 500)
        self.setStyleSheet("#AddUI { background-color: #F0F5F9; }")

        self.titleBar.maxBtn.deleteLater()  # 移除最大化按钮
        self.titleBar.minBtn.deleteLater()  # 移除最大化按钮

        self.__searchbut.setIconSize(QSize(20,20))
        self.__searchbut.setIcon(QIcon("D:/python/CatChat/res/loupe.png"))

        # 為布局添加控件並設置伸縮因子
        self.__Hlayout.addWidget(self.__searchber)
        self.__Hlayout.addWidget(self.__searchbut)
        self.__Vlayout.addLayout(self.__Hlayout)
