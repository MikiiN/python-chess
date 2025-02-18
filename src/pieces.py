import enum

class PieceType(enum.Enum):
    WHITE = True
    BLACK = False


class Piece:
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
        self.x = new_x
        self.y = new_y
    


class King(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)



class Queen(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)



class Bishop(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        


class Knight(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        


class Rook(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)
        


class Pawn(Piece):
    def __init__(
        self,
        x: int,
        y: int,
        p_type: PieceType
    ):
        super().__init__(x, y, p_type)