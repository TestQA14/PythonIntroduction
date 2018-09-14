from Classes.SquareClass import Square


class DoubleSquare(Square):

    def __init__(self,x):
        self.x = 2 * x
        self.y = x

    def perimeter(self):
        return 2 *self.x + 3 * self.y