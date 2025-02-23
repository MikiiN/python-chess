from __future__ import annotations
import enum

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
    
    
    def is_space_empty(self, x: int, y: int):
        return self.board[x][y] == None
    
    
    def get_piece_available_moves(self, piece: Piece):
        # piece_type = type(piece)
        # if piece_type is King:
        #     pass
        # elif piece_type is Queen:
        #     pass
        # elif piece_type is Bishop:
        #     pass
        # elif piece_type is Knight:
        #     pass
        # elif piece_type is Rook:
        #     pass
        # elif piece_type is Pawn:
        #     pass
        # else:
        #     raise RuntimeError('Invalid piece type')
        pass



class PieceType(enum.Enum):
    WHITE = True
    BLACK = False



class Piece:
    MAX_POS = 7
    MIN_POS = 0
    
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType,
        shifts: list[tuple[int, int]]
    ):    
        self.x = x
        self.y = y
        self.type = p_type
        self.available_moves = None
        self._SHIFTS = shifts
    
    
    def move(self, new_x, new_y):
        if self.MIN_POS <= new_x <= self.MAX_POS \
            and self.MIN_POS <= new_y <= self.MAX_POS: 
            self.x = new_x
            self.y = new_y
            self.available_moves = None
        else:
            raise RuntimeError("Invalid position")
    
    
    def is_same_color(self, other: Piece):
        return self.type.value == other.type.value
    
    
    def _calculate_new_pos(self, shift: tuple[int, int]):
        return (self.x+shift[0], self.y+shift[1])
    
    
    def _is_in_board(self, pos: tuple):
        if pos[0] < self.MIN_POS or pos[1] < self.MIN_POS:
            return False
        if pos[0] > self.MAX_POS or pos[1] > self.MAX_POS:
            return False
        return True
    
    
    # TODO need optimization
    # get all possible piece moves
    def _get_moves(self, board: Board):
        result = []
        for shift in self._SHIFTS:
            pos = (self.x + shift[0], self.y + shift[1])
            if not self._is_in_board(pos):
                continue
            result.append(pos)
        return result

    
    def get_moves(self, board: Board):
        if self.available_moves == None:
            self.available_moves = self._get_moves(board)
        return self.available_moves
    
    
    def get_shifts(self):
        return self._SHIFTS
    


class King(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = [
            (-1, -1), (1, -1), (-1, 1), (1, 1), 
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        super().__init__(x, y, p_type, shifts)
    
    
    # TODO need to look for checks
    def _get_moves(self, board: Board):
        pass



class Queen(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = [
            (-1, -1), (1, -1), (-1, 1), (1, 1), 
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        super().__init__(x, y, p_type, shifts)

    
    def _get_moves(self, board: Board):
        shifts = self.get_shifts()
        result = []
        for shift in shifts:
            for i in range(1, 8):
                pos = self._calculate_new_pos(
                    tuple([x*i for x in shift])
                )
                if not self._is_in_board(pos):
                    break
                piece = board.get_piece_by_pos(pos[0], pos[1])
                if piece == None:
                    result.append(pos)
                elif not self.is_same_color(piece):
                    result.append(pos)
                    break
                else:
                    break
        return result
                


class Bishop(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = [
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        super().__init__(x, y, p_type, shifts)
    


class Knight(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = [
            (-2, -1), (2, -1), (-2, 1), (2, 1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        super().__init__(x, y, p_type, shifts)
        


class Rook(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        super().__init__(x, y, p_type, shifts)
        


class Pawn(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = [
            (1, -1), (1, 1), (1, 0), (2, 0)
        ]
        super().__init__(x, y, p_type, shifts)