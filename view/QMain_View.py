from PyQt6 import QtCore, QtGui, QtWidgets
from qframelesswindow import FramelessWindow


class MainFrame(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MainUI")
        self.resize(1200, 700)
        self.setFixedSize(1200, 700)
        # Set size policy and stylesheet in one step
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        self.setStyleSheet("#MainUI { background-color: rgb(255, 255, 255); }")

        # Main layout setup
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setContentsMargins(30, 45, 30, -1)
        self.verticalLayout_2.setSpacing(10)

        # VLayout setup with MainLayout and navigation layout
        self.VLayout = QtWidgets.QVBoxLayout()
        self.MainLayout = QtWidgets.QHBoxLayout()
        self.VLayout.addLayout(self.MainLayout)

        # Navigation layout setup with spacer items and navigation bar
        self.navigationlayout = QtWidgets.QHBoxLayout()
        self.navigationlayout.setSpacing(15)
        self.navigationlayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                            QtWidgets.QSizePolicy.Policy.Minimum))

        # Navigation bar setup
        self.navigationbar = QtWidgets.QWidget(self)
        self.navigationbar.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.navigationbar.setFixedSize(400, 40)
        self.navigationbar.setStyleSheet("QWidget { background-color: rgb(255, 255, 255); border-radius: 20px; border: 1px solid #E0E0E0}")

        self.navigationlayout.addWidget(self.navigationbar, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
        self.navigationlayout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                            QtWidgets.QSizePolicy.Policy.Minimum))

        # Add layouts to the main layout
        self.VLayout.addLayout(self.navigationlayout)
        self.verticalLayout_2.addLayout(self.VLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainUI", "MainUI"))
