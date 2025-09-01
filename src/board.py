from __future__ import annotations
from typing import List, Dict
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
        self.up_player = up_player
        self.down_player = down_player
    
        # store pieces in array
        self.pieces : Dict[List[Piece]]
        self.pieces[self.up_player] = []
        self.pieces[self.down_player] = []
        for i in range(0, 2):
            for j in range(0, 8):
                self.pieces[self.up_player].append(self.board[i][j])
                self.pieces[self.down_player].append(self.board[i+6][j])        
    
    
    def get_piece_by_pos(self, x: int, y: int) -> Piece:
        try:
            return self.board[x][y]
        except Exception:
            raise RuntimeError("Invalid board position")
    
    
    def get_king(self, player: PieceType):
        for piece in self.pieces[player]:
            if isinstance(piece, King):
                return piece
        
    
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
        return piece.get_moves(self)
    
    
    def is_pos_threatened_by_opponent(self, player: PieceType, x, y):
        opponent = PieceType(not player.value)
        for opponent_piece in self.pieces[opponent]:
            if opponent_piece.is_threating_pos(x, y, self):
                return True
        return False



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

    
    def is_threating_pos(self, x, y, board: Board):
        moves = self.get_moves(board)
        return (x, y) in moves 
    
    
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
        self.moved = False
        super().__init__(x, y, p_type, shifts)
    
    
    def move(self, new_x, new_y):
        self.moved = True
        super().move(new_x, new_y)
    
    
    def _is_check(self, x, y, board: Board):
        return board.is_pos_threatened_by_opponent(
            self.type,
            x, y
        )
    
    def is_check(self, board: Board):
        return self._is_check(self.x, self.y, board)
    
    
    def get_moves(self, board: Board):
        self.available_moves = []
        available_moves = self._get_moves(board)
        for move in available_moves:
            if not self._is_check(move[0], move[1], board):
                self.available_moves.append(move)
        return self.available_moves
    
    
    def is_mate(self, board: Board):
        moves = self.get_moves(board)
        return moves == []
            


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
    
    
    def _get_moves(self, board: Board):
        result = []
        for shift in self._SHIFTS:
            pos = self._calculate_new_pos(shift)
            if not self._is_in_board(pos):
                continue
            if not board.is_space_empty(pos):
                continue
            piece = board.get_piece_by_pos(pos[0], pos[1])
            if self.is_same_color(piece):
                continue 
            result.append(pos)
        return result
        


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
        self.moved = False
        super().__init__(x, y, p_type, shifts)
        
    
    def move(self, new_x, new_y):
        self.moved = True
        super().move(new_x, new_y)



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
    
    
    # TODO need some love (ugly implementation)
    def _get_moves(self, board: Board):
        result = []
        if self.type == board.up_player:
            direction = -1
        else:
            direction = 1
            
        pos_forward = self._calculate_new_pos((direction, 0))
        if self._is_in_board(pos_forward):
            if board.is_space_empty(pos_forward[0], pos_forward[1]):
                result.append(pos_forward)
        if self.x == 1 and self.type == board.up_player \
            or self.x == 6 and self.type == board.down_player:
            pos_forward = self._calculate_new_pos((direction*2, 0))
            if self._is_in_board(pos_forward):
                if board.is_space_empty(pos_forward[0], pos_forward[1]):
                    result.append(pos_forward)
        
        pos_left = self._calculate_new_pos((direction, -direction))
        if self._is_in_board(pos_left):
            piece = board.get_piece_by_pos(pos_left[0], pos_left[1])
            if piece != None:
                if not self.is_same_color(piece):
                    result.append(pos_left)
        
        pos_right = self._calculate_new_pos((direction, direction))
        if self._is_in_board(pos_right):
            piece = board.get_piece_by_pos(pos_right[0], pos_right[1])
            if piece != None:
                if not self.is_same_color(piece):
                    result.append(pos_right)
        return result