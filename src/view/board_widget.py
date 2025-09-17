from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem

from src.view.ui.board_widget_ui import Ui_BoardWidget


class WhiteSpace(QGraphicsItem):
    def __init__(self, x, y):
        pass



class BoardWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_BoardWidget()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene()
        

        board = QGraphicsPixmapItem(QPixmap("img/board.png"))
        self.scene.addItem(board)
        self.ui.graphicsView.setScene(self.scene)