from src.pieces import King, Queen, Bishop, Knight, Rook, Pawn, PieceType, Piece

class Board:
    def __init__(self, player: PieceType):
        up_player = PieceType(not player.value)
        down_player = player
        self.board = [
            [
                Rook(0, 0, up_player), Knight(0, 1, up_player), 
                Bishop(0, 2, up_player), Queen(0, 3, up_player), 
                King(0, 4, up_player), Bishop(0, 5, up_player), 
                Knight(0, 6, up_player), Rook(0, 7, up_player)
            ],
            [Pawn(1, i, up_player) for i in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [Pawn(6, i, down_player) for i in range(8)],
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
            raise RuntimeError("Unknown board position")
        
    
    def move_piece(
        self, 
        piece: Piece, 
        new_x: int,
        new_y: int
    ):
        self.board[piece.x][piece.y] = None
        piece.move(new_x, new_y)
        self.board[new_x][new_y] = piece