from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QLabel


class QCircleimage(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QSize(100, 100))
        self.__pixmap = None
        self.__mask = None

    def setimage(self, filename: str):
        self.__pixmap = QPixmap(filename)
        self.__pixmap = self.__pixmap.scaled(self.__pixmap.width(), self.__pixmap.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.__mask = QBitmap(self.__pixmap.size())

        painter = QPainter(self.__mask)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        painter.fillRect(self.__mask.rect(), Qt.GlobalColor.white)

        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawRoundedRect(self.__pixmap.rect(), self.__pixmap.size().width(), self.__pixmap.size().height())
        painter.end()

        self.__pixmap.setMask(self.__mask)
        self.setPixmap(self.__pixmap)
        self.setScaledContents(True)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == event.button().LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)