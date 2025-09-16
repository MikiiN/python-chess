from PySide6.QtWidgets import QMainWindow

from src.constants import GameMode, PlayerColor
from src.view.ui.main_window_ui import Ui_MainWindow
from src.view.menu_widget import MenuWidget
from src.view.choose_side_widget import ChooseSideWidget


class MainWindow(QMainWindow):    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Chess Game")
        self.chosen_game_mode = None
        self.chosen_color = None
        self.widget_dict = {}
        self.widget_list = []
        self._init_widgets()
        self._append_widgets()
        

    def _init_widgets(self):
        self.widget_list = [
            MenuWidget(self),
            ChooseSideWidget(self)
        ]
    
    
    def _append_widgets(self):
        for i, widget in enumerate(self.widget_list):
            self.widget_dict[widget] = i
            self.ui.stackedWidget.addWidget(widget)
            
    
    def one_player_clicked(self):
        self.chosen_game_mode = GameMode.ONE_PLAYER
        self.ui.stackedWidget.setCurrentIndex(1)
        
    
    def two_player_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    
    def play_as_white_clicked(self):
        self.chosen_color = PlayerColor.WHITE
        self.ui.stackedWidget.setCurrentIndex(1)
        
    
    def play_as_black_clicked(self):
        self.chosen_color = PlayerColor.BLACK
        self.ui.stackedWidget.setCurrentIndex(1)