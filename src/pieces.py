class __Piece:
    def __init__(
        self,
        x: int,
        y: int
    ):    
        self.x = x
        self.y = y
        


class King(__Piece):
    def __init__(
        self,
        x: int,
        y: int
    ):
        super().__init__(x, y)



class Queen(__Piece):
    def __init__(
        self,
        x: int,
        y: int
    ):
        super().__init__(x, y)



class Bishop(__Piece):
    def __init__(
        self,
        x: int,
        y: int
    ):
        super().__init__(x, y)
        


class Knight(__Piece):
    def __init__(
        self,
        x: int,
        y: int
    ):
        super().__init__(x, y)
        


class Rook(__Piece):
    def __init__(
        self,
        x: int,
        y: int
    ):
        super().__init__(x, y)
        


class Pawn(__Piece):
    def __init__(
        self,
        x: int,
        y: int
    ):
        super().__init__(x, y)