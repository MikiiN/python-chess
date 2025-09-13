from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from src.view.ui.menu_widget_ui import Ui_MenuWidget


class MenuWidget(QWidget):
    def __init__(self, main_window):
        super(MenuWidget, self).__init__()
        self.ui = Ui_MenuWidget()
        self.ui.setupUi(self)
        self.ui.logoLabel.setPixmap(QPixmap('img/chess_game_icon.png'))
        self.ui.logoLabel.setScaledContents(True)
        self.ui.onePlayerButton.clicked.connect(main_window.one_player_clicked)