from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLabel

from .QChangeButton import QChangeButton

class QFullinformation(QtWidgets.QWidget):
    def __init__(self, parent=None, uuid:str=None):
        super().__init__(parent)
        self.__uuid = uuid
        # information_Box 的佈局設置
        self.informat_vlayout = QtWidgets.QVBoxLayout(self)
        # information bottom 設置
        self.bottom_widget = QtWidgets.QWidget(self)
        self.bottom_layout = QtWidgets.QVBoxLayout(self.bottom_widget)
        # information 內容設置
        self.name_label = QLabel(self.bottom_widget)
        self.uuid_label = QLabel(self.bottom_widget)

        # share Button
        self.share_button = QChangeButton(self, "D:/python/CatChat/res/share.png", "D:/python/CatChat/res/tick.png")
        self.share_button.set_time(1000)
        self.share_button.setStyleSheet("""
        QPushButton {
            background-color: rgba(242, 242, 242, 235);
            border-radius: 17px;
        }
        """)
        self.share_button.setFixedSize(35, 35)

        # 設置固定大小
        self.resize(250, 250)
        self.setMinimumSize(250, 250)
        self.setMaximumSize(250, 250)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.setObjectName("information_Box")

        # 使用樣式表來設置背景圖片和圓角效果
        self.setStyleSheet("""#information_Box {
            background-color: #BBFFFF;
            border-radius: 25px;
            border-image: url('D:/python/CatChat/res/avatar.jpg');
            }""")
        self.setContentsMargins(0, 0, 0, 0)

        # 所有QWidgets的設置初始
        self.ui_init()

        # 確保widget可見
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)

    def ui_init(self):
        self.bottom_widget.setFixedSize(self.width() / 1.1, self.height() / 4)
        self.bottom_widget.setObjectName("Bottm_Widget")
        self.bottom_widget.setStyleSheet("""
        #Bottm_Widget {
           background: rgba(242, 242, 242, 235);
           border-radius: 20px;
        }
        """)
        self.informat_vlayout.addWidget(self.share_button, alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignRight)
        self.informat_vlayout.addWidget(self.bottom_widget, alignment=QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignBottom)
        self.bottom_widget.setContentsMargins(0, 0, 0, 0)

        self.name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.name_label.setText("QAQ")
        self.name_label.setObjectName("Name_Lable")
        self.name_label.setStyleSheet("""
        #Name_Lable {
            font-family: Arial Black;
            font-size: 20px;
            color: #594E3F;
        }
        """)
        self.uuid_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.uuid_label.setText(f"UUID: {self.__uuid}")
        self.uuid_label.setObjectName("UUID_Lable")
        self.uuid_label.setStyleSheet("""
        #UUID_Lable {
            font-size: 10px;
            color: #594E3F;
        }
        """)

        self.bottom_layout.addWidget(self.name_label,
                                     alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.bottom_layout.addWidget(self.uuid_label,
                                     alignment=QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter)


    def setuuid(self, uuid:str=None):
        self.__uuid = uuid
        self.uuid_label.update()