from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import QAbstractAnimation, QVariantAnimation, QSize, QEasingCurve
from PyQt6.QtGui import QPixmap, QTransform, QIcon
from PyQt6.QtWidgets import QPushButton

class QChangeButton(QPushButton):
    def __init__(self, parent=None, icon:str=None, finishicon:str=None):
        super().__init__(parent=parent)
        self.__icon = icon
        self.__finish = finishicon
        self.setFixedSize(25, 25)
        self.setObjectName("add_button")
        self.setStyleSheet("""
        #add_button {
           border: none;
        }
        """)
        self.setIconSize(QSize(15, 15))
        self.iconpixmap = QPixmap(self.__icon)
        self.new_iconpixmap = QPixmap(self.__finish)  # 加載新的圖標
        self.is_rotated = False                    # 記錄圖標是否已更換
        self.setIcon(QIcon(self.iconpixmap))
        # 設置動畫
        self.animation = QVariantAnimation(self)
        self.animation.setEasingCurve(QEasingCurve.Type.InQuad)
        self.animation.setDuration(600)  # 動畫時長 500 毫秒
        self.animation.setStartValue(0)
        self.animation.setEndValue(180)
        self.animation.valueChanged.connect(self.update_icon)
        self.animation.finished.connect(self.switch_icon)  # 動畫結束後切換圖標

        # 點擊時觸發旋轉動畫
        self.clicked.connect(self.start_rotation)

    def start_rotation(self):
        # 如果動畫正在運行則忽略點擊
        if self.animation.state() == QAbstractAnimation.State.Running:
            return
        # 啟動動畫
        self.animation.start()

    def update_icon(self, angle):
        # 根據動畫值旋轉圖標並更新按鈕顯示
        trans = QTransform().rotate(angle)
        pixmap_to_rotate = self.new_iconpixmap if self.is_rotated else self.iconpixmap
        rotated_pixmap = pixmap_to_rotate.transformed(trans)
        self.setIcon(QtGui.QIcon(rotated_pixmap))

    def switch_icon(self):
        # 切換圖標狀態
        self.is_rotated = not self.is_rotated
        # 在動畫結束後顯示新圖標
        final_pixmap = self.new_iconpixmap if self.is_rotated else self.iconpixmap
        self.setIcon(QtGui.QIcon(final_pixmap))