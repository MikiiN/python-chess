from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from src.view.ui.choose_side_widget_ui import Ui_ChooseSideWidget


class ChooseSideWidget(QWidget):
    def __init__(self, main_window):
        super(ChooseSideWidget, self).__init__()
        self.ui = Ui_ChooseSideWidget()
        self.ui.setupUi(self)
        self.ui.logoLabel.setPixmap(QPixmap('img/chess_game_icon.png'))
        self.ui.logoLabel.setScaledContents(True)
        self.ui.whitePlayerButton.clicked.connect(main_window.play_as_white_clicked)
        self.ui.blackPlayerButton.clicked.connect(main_window.play_as_black_clicked)