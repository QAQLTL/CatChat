from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QAbstractAnimation, QVariantAnimation, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtWidgets import QListWidget


class QTitlebar(QtWidgets.QWidget):
    titlebar_signal = pyqtSignal(str)

    def __init__(self, parent=None, title: str = None):
        super().__init__(parent=parent)
        self.__title = title
        self._angle = [0, 180]  # 初始化角度
        self.iconpixmap = QPixmap("D:/python/CatChat/res/down.png")  # 加載圖片

        # 設置動畫
        self.animation = QVariantAnimation(self)

        # 設置界面
        self.resize(250, 40)
        self.topbarHlay = QtWidgets.QHBoxLayout(self)
        self.titleLable = QtWidgets.QLabel(self)
        self.iconlable = QtWidgets.QLabel(self)

        self.ui_init()

    def ui_init(self):
        # 設置標題
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

        # 設置 iconlable 大小
        self.iconlable.setFixedSize(15, 15)
        self.iconlable.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.topbarHlay.addWidget(self.iconlable, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

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

class QFramelessmenu(QtWidgets.QWidget):
    def __init__(self, parent=None, title: str = None):
        super().__init__(parent=parent)
        self.__title = title
        self.__datalist = []

        self.Vlayout = QtWidgets.QVBoxLayout(self)
        self.__topbar = QTitlebar(parent=self, title=self.__title)
        self.__listview = QListWidget(self)
        self.ui_init()

    def ui_init(self):
        self.resize(250, 250)
        self.setMinimumSize(250, 250)
        self.setMaximumSize(250, 800)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)

        self.Vlayout.addWidget(self.__topbar, alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        self.__listview.resize(200, 800)
        self.Vlayout.addWidget(self.__listview, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
