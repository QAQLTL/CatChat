from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QAbstractAnimation, QVariantAnimation, pyqtSignal, QSize, QEasingCurve
from PyQt6.QtGui import QPixmap, QTransform, QIcon, QColor
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QHBoxLayout, QLabel, QPushButton, QVBoxLayout

from .QChangeButton import QChangeButton
from .QCircleimage import QCircleimage

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
        self.button = QChangeButton(self.widget, "D:/python/CatChat/res/add-user.png",
                                    "D:/python/CatChat/res/delete.png")

        self.widget.mousePressEvent = self.handle_widget_click

        self.ui_init()

    def ui_init(self):
        self.Hlayout.setSpacing(15)
        self.Hlayout.setContentsMargins(10, 0, 20, 0)  # 移除內邊距

        self.Vlayout.setSpacing(0)
        self.Vlayout.setContentsMargins(0, 10, 0, 10)  # 移除內邊距

        self.setSizeHint(QSize(250, 60))

        self.widget.setObjectName("mainwidget")

        self.Cimg.setFixedSize(55, 55)
        self.Cimg.setimage(self.__avatar)
        self.Cimg.setborder()

        font = QtGui.QFont()
        font.setFamily('Arial Black')
        self.name_label.setText(self.__name)
        self.name_label.setObjectName("Name_Lable")
        self.name_label.setStyleSheet("""
        #Name_Lable {
            font-size: 14px;
            color: rgb(99,102,102);
        }
        """)
        self.name_label.setFont(font)
        self.uuid_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.uuid_label.setText(f"UUID: {self.__uuid}")
        self.uuid_label.setObjectName("UUID_Lable")
        self.uuid_label.setStyleSheet("""
        #UUID_Lable {
            font-size: 10px;
            color: rgb(99,102,102);
        }
        """)

        self.Hlayout.addWidget(self.Cimg, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Hlayout.addLayout(self.Vlayout)
        self.Vlayout.addWidget(self.name_label, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Vlayout.addWidget(self.uuid_label, 0, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Hlayout.addWidget(self.button, 1, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

    def handle_widget_click(self, event):
        """處理 widget 點擊事件，並觸發按鈕旋轉動畫。"""
        self.button.start_rotation()

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
        self.animation.setEasingCurve(QEasingCurve.Type.InQuad)

        # 設置界面
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
           font-size: 14px;
           color: rgb(99,102,102);
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
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui_init()

    def ui_init(self):
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.setSpacing(1)

        self.setObjectName("ListW")
        self.setStyleSheet("""
        #ListW {
            background-color: rgb(242,242,242);
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
        self.resize(250, 350)
        self.setMinimumSize(250, 350)
        self.setMaximumSize(250, 350)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)

        self.Vlayout.setSpacing(0)
        self.Vlayout.setContentsMargins(0,0,0,0)

        self.Vlayout.addWidget(self.__topbar, 0, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        self.Vlayout.addWidget(self.__listview, 1, alignment=QtCore.Qt.AlignmentFlag.AlignTop)