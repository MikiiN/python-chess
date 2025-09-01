import enum
import src.board as brd


# for future use
class GameMode(enum.Enum):
    PLAYER_VS_COMPUTER = 0



class Game:
    def __init__(self, player_color: brd.PieceType, game_mode: GameMode):
        self.mode = game_mode
        self.board = brd.Board(player_color)
        self.turn = brd.PieceType.WHITE
        
    
    def step(
        self, 
        player: brd.PieceType,
        x: int, y: int,
        new_x: int, new_y: int 
    ):
        if player != self.turn:
            raise RuntimeError("Not player's turn")
        
        piece = self.board.get_piece_by_pos(x, y)
        self.board.move_piece(piece, new_x, new_y)
        self.turn = brd.PieceType(not self.turn)
    
    
    def is_game_over(self):
        black_king = self.board.get_king(brd.PieceType.BLACK)
        white_king = self.board.get_king(brd.PieceType.WHITE)
        
        return black_king.is_mate(self.board) or white_king.is_mate(self.board)