from .UiSlp import Ui_Setting

from PyQt6.QtWidgets import QFrame

class SettingInterFace(QFrame, Ui_Setting):
    def __init__(self, parent):
        super().__init__(parent=parent)
