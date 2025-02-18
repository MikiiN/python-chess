import enum

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
        self.next_moves = None
        self._SHIFTS = shifts
    
    
    def move(self, new_x, new_y):
        if self.MIN_POS <= new_x <= self.MAX_POS \
            and self.MIN_POS <= new_y <= self.MAX_POS: 
            self.x = new_x
            self.y = new_y
            self.next_moves = None
        else:
            raise RuntimeError("Invalid position")
    
    
    # TODO need optimization
    # get all possible piece moves (moves against game logic too)
    def _get_all_moves(self, shifts: list[tuple[int, int]]):
        result = []
        for shift in shifts:
            pos = (self.x + shift[0], self.y + shift[1])
            if self.MIN_POS <= pos[0] <= self.MAX_POS \
                and self.MIN_POS <= pos[1] <= self.MAX_POS:
                result.append(pos)
        return result

    
    def get_all_moves(self):
        if self.next_moves == None:
            self.next_moves = self._get_all_moves(self._SHIFTS)
        return self.next_moves
    


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



class Queen(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = []
        # store all possible shifts
        for i in range(8):
            shifts.append((i, i))
            shifts.append((-i, -i))
            shifts.append((i, -i))
            shifts.append((-i, i))
            shifts.append((i, 0))
            shifts.append((-i, 0))
            shifts.append((0, i))
            shifts.append((0, -i))
        super().__init__(x, y, p_type, shifts)



class Bishop(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        shifts = []
        # store all possible shifts
        for i in range(8):
            shifts.append((i, i))
            shifts.append((-i, -i))
            shifts.append((i, -i))
            shifts.append((-i, i))
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
        shifts = []
        # store all possible shifts
        for i in range(8):
            shifts.append((i, 0))
            shifts.append((-i, 0))
            shifts.append((0, i))
            shifts.append((0, -i))
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