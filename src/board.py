from src.pieces import King, Queen, Bishop, Knight, Rook, Pawn, PieceType, Piece

class Board:
    BOARD_SIZE = 8
    
    def __init__(self, player: PieceType):
        # determine on which half will be white and black
        up_player = PieceType(not player.value)
        down_player = player
        
        # default board position
        self.board = [
            [
                Rook(0, 0, up_player), Knight(0, 1, up_player), 
                Bishop(0, 2, up_player), Queen(0, 3, up_player), 
                King(0, 4, up_player), Bishop(0, 5, up_player), 
                Knight(0, 6, up_player), Rook(0, 7, up_player)
            ],
            [Pawn(1, i, up_player) for i in range(self.BOARD_SIZE)],
            [None for _ in range(self.BOARD_SIZE)],
            [None for _ in range(self.BOARD_SIZE)],
            [None for _ in range(self.BOARD_SIZE)],
            [None for _ in range(self.BOARD_SIZE)],
            [Pawn(6, i, down_player) for i in range(self.BOARD_SIZE)],
            [
                Rook(7, 0, down_player), Knight(7, 1, down_player), 
                Bishop(7, 2, down_player), Queen(7, 3, down_player), 
                King(7, 4, down_player), Bishop(7, 5, down_player), 
                Knight(7, 6, down_player), Rook(7, 7, down_player)
            ],
        ]
    
    
    def get_piece_by_pos(self, x: int, y: int):
        try:
            return self.board[x][y]
        except Exception:
            raise RuntimeError("Invalid board position")
        
    
    def move_piece(
        self, 
        piece: Piece, 
        new_x: int,
        new_y: int
    ):
        self.board[piece.x][piece.y] = None
        try:
            piece.move(new_x, new_y)
            self.board[new_x][new_y] = piece
        except Exception:
            raise RuntimeError("Invalid board position")
    
    
    def get_piece_available_moves(self, piece: Piece):
        piece_type = type(piece)
        if piece_type is King:
            pass
        elif piece_type is Queen:
            pass
        elif piece_type is Bishop:
            pass
        elif piece_type is Knight:
            pass
        elif piece_type is Rook:
            pass
        elif piece_type is Pawn:
            pass
        else:
            raise RuntimeError('Invalid piece type')