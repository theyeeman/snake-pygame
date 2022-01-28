from Engine.doublylinkedlist import DoublyLinkedList
from Engine.direction import Direction


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


class Snake():
    def __init__(self, screen):
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.body_list = DoublyLinkedList()
        self.body_set = set()
        self.is_dead = False
        self.score = 0

        self.create_class_properties()

    def create_class_properties(self):
        head_x = self.screen_width // 2
        head_y = self.screen_height // 2
        self.body_list.append(Position(head_x, head_y, Direction.RIGHT))
        self.body_set.add(self.get_head())

    def get_head(self):
        return self.body_list.peek_beginning()

    def get_tail(self):
        return self.body_list.peek_end()

    def remove_tail(self):
        tail = self.body_list.pop_end()
        self.body_set.discard(tail)

    def insert_head(self, head):
        self.body_list.prepend(head)
        self.body_set.add(head)

    def overwrite_head(self, head):
        self.body_list.remove_beginning()
        self.body_list.prepend(head)

    def get_next_head(self):
        return self.get_next_position(self.get_head())

    def get_next_position(self, curr):
        if curr.direction == Direction.UP:
            new_head = Position(curr.x, curr.y - 1, curr.direction)
        elif curr.direction == Direction.RIGHT:
            new_head = Position(curr.x + 1, curr.y, curr.direction)
        elif curr.direction == Direction.DOWN:
            new_head = Position(curr.x, curr.y + 1, curr.direction)
        elif curr.direction == Direction.LEFT:
            new_head = Position(curr.x - 1, curr.y, curr.direction)

        return new_head

    def to_list_full(self):
        return self.body_list.to_list_full()
