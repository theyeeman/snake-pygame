class Position():
    def __init__(self, x, y, direction=None):
        self.x = x
        self.y = y
        self.direction = direction

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y