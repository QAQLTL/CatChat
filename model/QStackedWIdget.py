from PyQt6.QtWidgets import QStackedWidget, QLabel
from PyQt6.QtCore import *
from PyQt6.QtGui import QMouseEvent

class StackedWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.start_pos = None
        self.is_animating = False

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and not self.is_animating:
            self.start_pos = event.position()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and self.start_pos:
            end_pos = event.position()
            delta_x = end_pos.x() - self.start_pos.x()

            if abs(delta_x) > 50:
                if delta_x > 0:
                    self.animateToPage(self.currentIndex() - 1, "right")
                else:
                    self.animateToPage(self.currentIndex() + 1, "left")

            self.start_pos = None
        super().mouseReleaseEvent(event)

    def animateToPage(self, target_index, direction):
        if target_index < 0 or target_index >= self.count() or self.is_animating:
            return

        self.is_animating = True
        current_widget = self.currentWidget()
        target_widget = self.widget(target_index)

        width = self.frameRect().width()

        if direction == "left":
            target_widget.move(width, 0)
        else:
            target_widget.move(-width, 0)

        target_widget.show()

        current_animation = QPropertyAnimation(current_widget, b"pos", self)
        target_animation = QPropertyAnimation(target_widget, b"pos", self)

        current_animation.setDuration(300)
        target_animation.setDuration(300)

        current_animation.setStartValue(current_widget.pos())
        current_animation.setEndValue(QPoint(-width if direction == "left" else width, 0))

        target_animation.setStartValue(target_widget.pos())
        target_animation.setEndValue(QPoint(0, 0))

        def on_animation_finished():
            self.setCurrentIndex(target_index)
            target_widget.move(0, 0)
            self.is_animating = False

        target_animation.finished.connect(on_animation_finished)

        current_animation.start()
        target_animation.start()

    def get_page_name(self, index: int) -> str:
        """根據索引獲取頁面的名稱"""
        page = self.widget(index)  # 根據索引獲取頁面
        return page.objectName() if page else ""