from Engine.doublylinkedlist import DoublyLinkedList
from Engine.direction import Direction

class Snake():
    def __init__(self, screen):
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.body_list = DoublyLinkedList()
        self.body_set = set()
        self.is_dead = False
        self.empty_set = self._generate_empty_set()

        head_x = self.screen_width // 2
        head_y = self.screen_height // 2
        self.body_list.append((head_x, head_y, Direction.RIGHT))
        self.body_set.add((head_x, head_y))
        self.empty_set.discard((head_x, head_y))
        self.food = self.create_food()
        
    def _generate_empty_set(self):
        s = set()
        
        for i in range(self.screen_width):
            for j in range(self.screen_height):
                s.add((i, j))
        
        return s

    def get_head(self):
        return self.body_list.peek_beginning()

    def get_tail(self):
        return self.body_list.peek_end()

    def remove_tail(self):
        self.body_list.remove_end()

    def _is_border_intersection(self, new_head_x, new_head_y):
        pass

    def is_eat_food(self, food):
        head_x, head_y, direction = self.body_list.peek_beginning()
        if self.body_list.peek_beginning():
            pass

    def create_food(self):
        pass
