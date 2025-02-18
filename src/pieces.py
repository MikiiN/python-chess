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
        p_type: PieceType
    ):    
        self.x = x
        self.y = y
        self.type = p_type
    
    
    def move(self, new_x, new_y):
        if self.MIN_POS <= new_x <= self.MAX_POS \
            and self.MIN_POS <= new_y <= self.MAX_POS: 
            self.x = new_x
            self.y = new_y
        else:
            raise RuntimeError("Invalid position")
    
    
    # get all possible piece moves (moves against game logic too)
    def _get_all_moves(self, shifts: list[tuple[int, int]]):
        result = []
        for shift in shifts:
            pos = (self.x + shift[0], self.y + shift[1])
            if self.MIN_POS <= pos[0] <= self.MAX_POS \
                and self.MIN_POS <= pos[1] <= self.MAX_POS:
                result.append(pos)
        return result
    


class King(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        self._SHIFTS = [
            (-1, -1), (1, -1), (-1, 1), (1, 1), 
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
    
        
    def get_all_moves(self):
        self._get_all_moves(self._SHIFTS)



class Queen(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        self._SHIFTS = []
        # store all possible shifts
        for i in range(8):
            self._SHIFTS.append((i, i))
            self._SHIFTS.append((-i, -i))
            self._SHIFTS.append((i, -i))
            self._SHIFTS.append((-i, i))
            self._SHIFTS.append((i, 0))
            self._SHIFTS.append((-i, 0))
            self._SHIFTS.append((0, i))
            self._SHIFTS.append((0, -i))
    
    
    def get_all_moves(self):
        self._get_all_moves(self._SHIFTS)



class Bishop(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        self._SHIFTS = []
        # store all possible shifts
        for i in range(8):
            self._SHIFTS.append((i, i))
            self._SHIFTS.append((-i, -i))
            self._SHIFTS.append((i, -i))
            self._SHIFTS.append((-i, i))
    
       
    def get_all_moves(self):
        self._get_all_moves(self._SHIFTS)
    


class Knight(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        self._SHIFTS = [
            (-2, -1), (2, -1), (-2, 1), (2, 1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
    
        
    def get_all_moves(self):
        return self._get_all_moves(self._SHIFTS)
        


class Rook(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        self._SHIFTS = []
        # store all possible shifts
        for i in range(8):
            self._SHIFTS.append((i, 0))
            self._SHIFTS.append((-i, 0))
            self._SHIFTS.append((0, i))
            self._SHIFTS.append((0, -i))
    
        
    def get_all_moves(self):
        self._get_all_moves(self._SHIFTS)
        


class Pawn(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        self._SHIFTS = [
            (1, -1), (1, 1), (1, 0), (2, 0)
        ]
    
        
    def get_all_moves(self):
        self._get_all_moves(self._SHIFTS)