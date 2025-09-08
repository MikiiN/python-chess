from PySide6.QtWidgets import QWidget
from src.view.ui.menu_widget_ui import Ui_MenuWidget


class MenuWidget(QWidget):
    def __init__(self):
        super(MenuWidget, self).__init__()
        self.ui = Ui_MenuWidget()
        self.ui.setupUi(self)