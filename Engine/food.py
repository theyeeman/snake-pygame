class Food():
    def __init__(self, empty_space_set):
        # maybe don't need this class because I can put food in snake class
        self.x_pos, self.y_pos = empty_space_set.pop()