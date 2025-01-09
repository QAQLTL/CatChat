from PyQt6 import QtCore, QtGui, QtWidgets
from qframelesswindow import FramelessWindow

class MainFrame(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MainUI")
        # self.setFixedSize(1200, 700)
        # Set size policy and stylesheet in one step
        # self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.setStyleSheet("#MainUI { background-color: #F0F5F9; }")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.VLayout = QtWidgets.QVBoxLayout()
        self.VLayout.setContentsMargins(5, 10, 5, 10)

        self.verticalLayout_2.addLayout(self.VLayout)

        # set Buttom layout
        # self.buttomlayout = QtWidgets.QHBoxLayout()
        # self.buttomlayout.setContentsMargins(0,0,5,0)
        # self.verticalLayout_2.addLayout(self.buttomlayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainUI", "MainUI"))
