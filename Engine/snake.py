from Engine.doublylinkedlist import DoublyLinkedList
from Engine.direction import Direction
from pygame import Color


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
        self.body_list.append((head_x, head_y, Direction.RIGHT))
        self.body_set.add((head_x, head_y))
        self.empty_set = self.generate_empty_set()
        self.empty_set.discard((head_x, head_y))
        self.food = self.create_food()
    
    def generate_empty_set(self):
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
        tail = self.body_list.pop_end()
        x, y = self.get_xy(tail)
        self.body_set.discard((x, y))
        self.empty_set.add((x, y))

    def get_xy(self, head):
        return (head[0], head[1])

    def insert_head(self, head):
        x, y = self.get_xy(head)
        self.body_list.prepend(head)
        self.body_set.add((x, y))
        self.empty_set.discard((x, y))

    def update_head(self, head):
        self.body_list.remove_beginning()
        self.body_list.prepend(head)

    def is_border_intersection(self, new_head_x, new_head_y):
        if new_head_x >= self.screen_width or new_head_x < 0:
            return True

        if new_head_y >= self.screen_height or new_head_y < 0:
            return True

        return False

    def is_snake_eating_itself(self, new_head_x, new_head_y):
        return (new_head_x, new_head_y) in self.body_set

    def is_snake_die(self, new_head_x, new_head_y):
        return (self.is_snake_eating_itself(new_head_x, new_head_y)
            or self.is_border_intersection(new_head_x, new_head_y))
    
    def is_eat_food(self):
        head_x, head_y = self.get_xy(self.body_list.peek_beginning())
        food_x, food_y = self.food

        if head_x == food_x and head_y == food_y:
            return True

        return False

    def create_food(self):
        food = self.empty_set.pop()
        self.empty_set.add(food)

        return food
        
    def to_list(self):
        return self.body_list.to_list()

