from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLabel

from .QCircleimage import QCircleImage


class QHInformat(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(250, 500)
        sizepolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizepolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizepolicy)
        self.setMinimumSize(QtCore.QSize(250, 250))
        # self.setMaximumSize(QtCore.QSize(250, 250))

        # 創建並添加 informat_widget
        self.informat_widget = QtWidgets.QWidget(parent=self)
        self.informat_widget.setObjectName("Information_Box")
        self.informat_widget.setStyleSheet(
            "#Information_Box {\n"
            "background: #BBFFFF;\n"
            "border-radius: 20px;\n"
            "}"
        )

        # informat_widget 的佈局設置
        self.informat_vlayout = QtWidgets.QVBoxLayout(self.informat_widget)
        self.informat_vlayout.setSpacing(0)

        # 設置頭像
        self.cr_img = QCircleImage(self)
        self.cr_img.setimage("res/avatar.jpg")
        self.cr_img.setborder()
        # shadow
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setXOffset(1)
        shadow.setYOffset(1)
        shadow.setBlurRadius(20)
        shadow.setColor(QtGui.QColor(0, 0, 0, 200))
        self.cr_img.setGraphicsEffect(shadow)
        self.informat_vlayout.addWidget(self.cr_img, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        #設置名稱
        font = QtGui.QFont()
        font.setFamily('Microsoft Sans Serif')
        font.setPointSize(12)
        self.name = QLabel(self)
        self.name.setText("QAQ")
        self.name.setFont(font)
        self.name.setStyleSheet("""
        color:#4F4F4F;
        """)
        self.informat_vlayout.addWidget(self.name, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)