from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QTimer

class GradientShadowEffect(QGraphicsDropShadowEffect):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBlurRadius(50)
        self.setOffset(0, 0)  # 無偏移

        # 顏色漸變參數
        self.current_color = QColor("red")
        self.target_color = QColor("blue")
        self.step = 0.02  # 每次顏色變化的步長
        self.progress = 0  # 進度值，從 0 到 1

        # 定時器控制漸變
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_shadow_color)
        self.timer.start(50)  # 每 50 毫秒更新一次顏色

    def update_shadow_color(self):
        # 根據進度值計算顏色插值
        r = self.interpolate(self.current_color.red(), self.target_color.red())
        g = self.interpolate(self.current_color.green(), self.target_color.green())
        b = self.interpolate(self.current_color.blue(), self.target_color.blue())

        # 更新陰影顏色
        self.setColor(QColor(int(r), int(g), int(b)))

        # 更新進度
        self.progress += self.step
        if self.progress >= 1:
            self.progress = 0
            # 交換顏色，形成循環漸變
            self.current_color, self.target_color = self.target_color, self.current_color

    def interpolate(self, start, end):
        """插值計算，根據進度計算顏色值"""
        return start + (end - start) * self.progress