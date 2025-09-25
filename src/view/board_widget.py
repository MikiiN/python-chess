from PySide6.QtCore import Qt, QRect, QRectF, QPointF
from PySide6.QtGui import QPixmap, QColor, QPainterPath, QBrush
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsItemGroup

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

            # add them to scene
            self.scene.addItem(white_piece)
            self.scene.addItem(white_pawn)
            self.scene.addItem(black_pawn)
            self.scene.addItem(black_piece)

            # set their starting position
            if self.down_player == PlayerColor.WHITE:
                black_piece.setPos(black_piece.mapFromScene(self.SQUARE_SIZE * col, 0))
                black_pawn.setPos(black_pawn.mapFromScene(self.SQUARE_SIZE * col, self.SQUARE_SIZE))
                white_piece.setPos(white_piece.mapFromScene(self.SQUARE_SIZE * col, (self.BOARD_SIZE-1)*self.SQUARE_SIZE))
                white_pawn.setPos(white_pawn.mapFromScene(self.SQUARE_SIZE * col, (self.BOARD_SIZE-2)*self.SQUARE_SIZE))
            else:
                white_piece.setPos(white_piece.mapFromScene(self.SQUARE_SIZE * col, 0))
                white_pawn.setPos(white_pawn.mapFromScene(self.SQUARE_SIZE * col, self.SQUARE_SIZE))
                black_piece.setPos(black_piece.mapFromScene(self.SQUARE_SIZE * col, (self.BOARD_SIZE-1)*self.SQUARE_SIZE))
                black_pawn.setPos(black_pawn.mapFromScene(self.SQUARE_SIZE * col, (self.BOARD_SIZE-2)*self.SQUARE_SIZE))



class ChessPiece(QGraphicsPixmapItem):
    def __init__(self, img_path, square_size):
        pixmap = PieceQPixmap(img_path, square_size).scaled(square_size, square_size)
        super().__init__(pixmap)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setShapeMode(self.ShapeMode.BoundingRectShape)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.old_pos = None
        self.square_size = square_size

    
    def mousePressEvent(self, event):
        # save piece's start position for invalid move
        self.old_pos = self.pos()
        return super().mousePressEvent(event)


    # TODO return to old pos for invalid moves
    def mouseReleaseEvent(self, event):
        point = self.scenePos()
        # calculate closest square to piece position when dropped
        new_x = abs(round(point.x() / self.square_size)) * self.square_size
        new_y = abs(round(point.y() / self.square_size)) * self.square_size
        self.setPos(new_x, new_y)
        self.old_pos = None
        super().mouseReleaseEvent(event)


    def itemChange(self, change, value):
        # make pieces not to leave chess board
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange and self.scene():
            new_pos = value
            scene_rect = self.scene().sceneRect()
            br = self.boundingRect()

            x = min(
                max(new_pos.x(), scene_rect.left()),
                scene_rect.right() - br.height()
            )
            y = min(
                max(new_pos.y(), scene_rect.top()),
                scene_rect.bottom() - br.height()
            )
            return QPointF(x, y)
        return super().itemChange(change, value)



class PieceQPixmap(QPixmap):
    def __init__(self, img_path, square_size):
        super().__init__(img_path)
        self.square_size = square_size

    
    def rect(self) -> QRect:
        return QRect(0, 0, self.square_size, self.square_size)