from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve


class QFullInformat(QtWidgets.QWidget):
    def __init__(self, parent=None, uuid:str=None):
        super().__init__(parent)
        self.__uuid = uuid

        # 設置固定大小
        self.resize(250, 250)
        self.setMinimumSize(250, 250)
        self.setMaximumSize(250, 250)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.setObjectName("information_Box")

        # 使用樣式表來設置背景圖片和圓角效果
        self.setStyleSheet(
            """#information_Box {
            background-color: #BBFFFF;
            border-radius: 20px;
            border-image: url('D:/python/CatChat/res/avatar.jpg');
            }"""
        )
        self.setContentsMargins(0, 0, 0, 0)

        # information_Box 的佈局設置
        self.informat_vlayout = QtWidgets.QVBoxLayout(self)
        self.bottom_widget = QtWidgets.QWidget(self)
        self.bottom_widget.setFixedSize(self.width() / 1.1, self.height() / 4)
        self.bottom_widget.setObjectName("Bottm_Widget")
        self.bottom_widget.setStyleSheet("""
        #Bottm_Widget {
           background:rgba(255, 255, 255, 240);
           border-radius: 15px;
        }
        """)
        self.informat_vlayout.addWidget(self.bottom_widget, alignment=QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignBottom)

        self.bottom_layout = QtWidgets.QVBoxLayout(self.bottom_widget)
        self.bottom_widget.setContentsMargins(0,0,0,0)

        font = QtGui.QFont()
        font.setFamily('Arial Black')
        self.name_label = QLabel(self.bottom_widget)
        self.name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.name_label.setText("QAQ")
        self.name_label.setStyleSheet("""
        font-size: 20px;
        color: gray;
        """)
        self.name_label.setFont(font)
        self.uuid_label = QLabel(self.bottom_widget)
        self.uuid_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.uuid_label.setText(f"UUID: {self.__uuid}")
        self.uuid_label.setStyleSheet("""
        font-size: 10px;
        color: gray;
        """)
        self.bottom_layout.addWidget(self.name_label,
                                     alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.bottom_layout.addWidget(self.uuid_label,
                                     alignment=QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignHCenter)

        # 確保widget可見
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)

    def setuuid(self, uuid:str=None):
        self.__uuid = uuid
        self.uuid_label.update()

    def enterEvent(self, event):
        # Start the animation with the current geometry
        start_geometry = self.geometry()
        # Define the new geometry with increased width and height
        end_geometry = QtCore.QRect(start_geometry.x(), start_geometry.y(), 300, 300)

        # Create the animation on the 'geometry' property
        self.anim = QPropertyAnimation(self, b"maximumsize")
        self.anim.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim.setDuration(1000)
        self.anim.setStartValue(start_geometry)
        self.anim.setEndValue(end_geometry)
        self.anim.start()
