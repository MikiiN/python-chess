from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPixmap, QColor, QPainterPath, QBrush
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem, QGraphicsRectItem

from src.view.ui.board_widget_ui import Ui_BoardWidget
from src.constants import PlayerColor

class WhiteSpace(QGraphicsItem):
    def __init__(self, x, y):
        pass



class BoardWidget(QWidget):
    SQUARE_SIZE = 80
    BOARD_SIZE = 8

    PIECES_WHITE_DOWN = [
        "rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"
    ]

    PIECES_WHITE_UP = [
        "rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook"
    ]

    def __init__(self, main_window, down_player: PlayerColor):
        super().__init__()
        self.down_player = down_player
        self.ui = Ui_BoardWidget()
        self.ui.setupUi(self)
        self.scene = self._create_board()
        self._deploy_pieces()
        
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setSceneRect(
            QRectF(
                0, 0,
                self.BOARD_SIZE * self.SQUARE_SIZE,
                self.BOARD_SIZE * self.SQUARE_SIZE 
            )
        )
    

    def _create_board(self) -> QGraphicsScene:
        scene = QGraphicsScene()
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                square = QGraphicsRectItem(
                    col * self.SQUARE_SIZE,
                    row * self.SQUARE_SIZE,
                    self.SQUARE_SIZE,
                    self.SQUARE_SIZE 
                )

                if (row + col) % 2:
                    square.setBrush(Qt.white)
                else:
                    square.setBrush(QColor(140, 80, 0))
                scene.addItem(square)
        return scene
    

    def _deploy_pieces(self):
        if self.down_player == PlayerColor.WHITE:
            pieces = self.PIECES_WHITE_DOWN
        else:
            pieces = self.PIECES_WHITE_UP

        for col, piece in enumerate(pieces):
            # create piece items
            white_piece = ChessPiece(f"img/white_{piece}.png", self.SQUARE_SIZE)
            white_pawn = ChessPiece("img/white_pawn.png", self.SQUARE_SIZE)
            black_piece = ChessPiece(f"img/black_{piece}.png", self.SQUARE_SIZE)
            black_pawn = ChessPiece("img/black_pawn.png", self.SQUARE_SIZE)

            # set their starting position
            if self.down_player == PlayerColor.WHITE:
                black_piece.setOffset(self.SQUARE_SIZE * col, 0)
                black_pawn.setOffset(self.SQUARE_SIZE * col, self.SQUARE_SIZE)
                white_piece.setOffset(self.SQUARE_SIZE * col, (self.BOARD_SIZE-1)*self.SQUARE_SIZE)
                white_pawn.setOffset(self.SQUARE_SIZE * col, (self.BOARD_SIZE-2)*self.SQUARE_SIZE)
            else:
                white_piece.setOffset(self.SQUARE_SIZE * col, 0)
                white_pawn.setOffset(self.SQUARE_SIZE * col, self.SQUARE_SIZE)
                black_piece.setOffset(self.SQUARE_SIZE * col, (self.BOARD_SIZE-1)*self.SQUARE_SIZE)
                black_pawn.setOffset(self.SQUARE_SIZE * col, (self.BOARD_SIZE-2)*self.SQUARE_SIZE)

            # add them to scene
            self.scene.addItem(white_piece)
            self.scene.addItem(white_pawn)
            self.scene.addItem(black_pawn)
            self.scene.addItem(black_piece)



class ChessPiece(QGraphicsRectItem):
    def __init__(self, img_path, square_size, parent=None):
        super().__init__(0, 0, square_size, square_size, parent)
        self.setBrush(QBrush(QColor(0, 0, 0, 0)))
        self.setFlag(QGraphicsRectItem.ItemIsMovable, True)
        self.square_size = square_size

        pixmap = QPixmap(img_path).scaled(square_size, square_size)
        self.piece = QGraphicsPixmapItem(pixmap, self)
        pw, ph = pixmap.width(), pixmap.height()
        self.piece.setPos((square_size - pw) / 2, (square_size - ph) / 2)
    

    def setOffset(self, x, y):
        self.setRect(x, y, self.square_size, self.square_size)