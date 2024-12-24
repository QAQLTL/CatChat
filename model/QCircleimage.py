from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QLabel


class QCircleimage(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(100, 100)
        self.__pixmap = None
        self.__mask = None

        self.__state = "#00EC00" or "#FF5151"

    def setimage(self, filename: str):
        """
        :param filename: input image location
        :return: None
        """

        # Load the image and set it as the pixmap for the label
        self.__pixmap = QPixmap(filename)
        self.__pixmap = self.__pixmap.scaled(self.__pixmap.width(), self.__pixmap.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # Create a mask the same shape as the image
        self.__mask = QBitmap(self.__pixmap.size())

        # Create a QPainter to draw the mask
        painter = QPainter(self.__mask)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        painter.fillRect(self.__mask.rect(), Qt.GlobalColor.white)

        # Draw a black, rounded rectangle on the mask
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawRoundedRect(self.__pixmap.rect(), self.__pixmap.size().width(), self.__pixmap.size().height())
        painter.end()

        # Apply the mask to the image
        self.__pixmap.setMask(self.__mask)
        self.setPixmap(self.__pixmap)
        self.setScaledContents(True)

    def setborder(self):
        self.setStyleSheet(f"""
        border: 2px Solid {self.__state};
        border-radius: 27%;
        padding: 1px 1px 1px 1px;
        """)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == event.button().LeftButton:  # 判斷是否左鍵
            self.clicked.emit()  # 觸發自訂信號
        super().mousePressEvent(event)  # 繼續執行父類別的 mousePressEvent