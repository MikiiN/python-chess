from PySide6.QtWidgets import QMainWindow

from src.view.ui.main_window_ui import Ui_MainWindow
from src.view.menu_widget import MenuWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.menu_widget = MenuWidget()
        self.ui.stackedWidget.addWidget(self.menu_widget)
