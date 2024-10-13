from PyQt6.QtWidgets import QStackedWidget, QHBoxLayout

from qfluentwidgets import (NavigationInterface, NavigationItemPosition)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar

from SocUi import *

class Window(FramelessWindow):
    def __init__(self):
        super().__init__()
        #set titlebar
        self.setTitleBar(StandardTitleBar(self))

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)

        #subset
        self.stackWidget = QStackedWidget(self)
        self.settingInterface = SettingInterFace(self)

        self.initLayout()
        self.initNavigation()

    def initLayout(self):
        self.hBoxLayout.setSpacing(5)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)


    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, parent=None):
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parent.objectName() if parent else None
        )

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)