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

        self.image_set = True  # 標記圖片已設置
        self.update()  # 刷新繪圖

    def paintEvent(self, event):
        if self.image_set:
            super().paintEvent(event)
            return

        super().paintEvent(event)
        
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

    def image(self):
        return self.imagepath is not None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == event.button().LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)