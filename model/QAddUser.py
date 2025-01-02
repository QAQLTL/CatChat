from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QCircleAddUser(QWidget):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui_init()

    def ui_init(self):
        self.setFixedSize(QSize(60, 60))  # 固定大小

    def paintEvent(self, event):
        # 初始化 QPainter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 绘制外部圆边
        pen = QPen(QColor("#B0AFBB"), 3)  # 设置边框颜色和宽度
        pen.setStyle(Qt.PenStyle.DotLine)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor("transparent")))  # 设置圆的填充颜色
        painter.drawEllipse(3, 3, self.width() - 6, self.height() - 6)

        # 绘制中间的 "+"
        pen.setStyle(Qt.PenStyle.SolidLine)
        pen.setColor(QColor("#B0AFBB"))  # 设置 "+" 的颜色
        pen.setWidth(4)
        painter.setPen(pen)
        # 计算中心点
        cx, cy = self.width() // 2, self.height() // 2
        # 画水平线
        painter.drawLine(cx - 10, cy, cx + 10, cy)
        # 画垂直线
        painter.drawLine(cx, cy - 10, cx, cy + 10)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == event.button().LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)