from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class QCircleAddUser(QWidget):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui_init()

    def ui_init(self):
        self.setFixedSize(QSize(60, 60))

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)


        pen = QPen(QColor("#B0AFBB"), 3)
        pen.setStyle(Qt.PenStyle.DotLine)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor("transparent")))
        painter.drawEllipse(3, 3, self.width() - 6, self.height() - 6)


        pen.setStyle(Qt.PenStyle.SolidLine)
        pen.setColor(QColor("#B0AFBB"))
        pen.setWidth(4)
        painter.setPen(pen)

        cx, cy = self.width() // 2, self.height() // 2

        painter.drawLine(cx - 10, cy, cx + 10, cy)

        painter.drawLine(cx, cy - 10, cx, cy + 10)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == event.button().LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)