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
        self.empty_set = set()
        self.is_dead = False

        self.create_class_properties()

    def create_class_properties(self):
        head_x = self.screen_width // 2
        head_y = self.screen_height // 2
        self.body_list.append(Position(head_x, head_y, Direction.RIGHT))
        self.body_set.add(self.get_head())
        self.empty_set = self.generate_empty_set()
        self.empty_set.discard(self.get_head())
        self.food = self.create_food()

    def generate_empty_set(self):
        s = set()

        for i in range(self.screen_width):
            for j in range(self.screen_height):
                s.add(Position(i, j))

        return s

    def get_head(self):
        return self.body_list.peek_beginning()

    def get_tail(self):
        return self.body_list.peek_end()

    def remove_tail(self):
        tail = self.body_list.pop_end()
        self.body_set.discard(tail)
        self.empty_set.add(tail)

    def insert_head(self, head):
        self.body_list.prepend(head)
        self.body_set.add(head)
        self.empty_set.discard(head)

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

    def is_border_intersection(self, head):
        if head.x >= self.screen_width or head.x < 0:
            return True

        if head.y >= self.screen_height or head.y < 0:
            return True

        return False

    def is_snake_eating_itself(self, head):
        return head in self.body_set

    def is_snake_die(self, head):
        return (self.is_snake_eating_itself(head)
                or self.is_border_intersection(head))

    def is_eat_food(self):
        if self.get_head() == self.food:
            return True

        return False

    def create_food(self):
        food = self.empty_set.pop()
        self.empty_set.add(food)

        return food

    def to_list_full(self):
        return self.body_list.to_list_full()
