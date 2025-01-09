from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QLabel


class QCircleimage(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(QSize(60, 60))
        self.imagepath = None
        self.__pixmap = None
        self.__mask = None
        self.image_set = False

    def setimage(self, filename: str):

        self.imagepath = filename
        self.__pixmap = QPixmap(filename)
        self.__pixmap = self.__pixmap.scaled(self.__pixmap.width(), self.__pixmap.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.__mask = QBitmap(self.__pixmap.size())

        imagepainter = QPainter(self.__mask)
        imagepainter.setRenderHint(QPainter.RenderHint.Antialiasing)
        imagepainter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        imagepainter.fillRect(self.__mask.rect(), Qt.GlobalColor.white)

        imagepainter.setPen(Qt.GlobalColor.black)
        imagepainter.setBrush(Qt.GlobalColor.black)
        imagepainter.drawRoundedRect(self.__pixmap.rect(), self.__pixmap.size().width(), self.__pixmap.size().height())
        imagepainter.end()

        self.__pixmap.setMask(self.__mask)
        self.setPixmap(self.__pixmap)
        self.setScaledContents(True)

        self.image_set = True
        self.update()

    def paintEvent(self, event):
        if self.image_set:
            super().paintEvent(event)
            return

        super().paintEvent(event)

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

    def image(self):
        return self.imagepath is not None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == event.button().LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)