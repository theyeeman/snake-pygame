from Engine.doublylinkedlist import DoublyLinkedList
from Engine.direction import Direction
from pygame import Color


class Snake():
    def __init__(self, screen):
        self.screen = screen
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
        temp = self.empty_set.pop()
        self.empty_set.add(temp)

        return temp

    def move_snake(self):
        curr_head_x, curr_head_y, curr_head_direction = self.get_head()
        new_head_direction = curr_head_direction

        if curr_head_direction == Direction.UP:
            new_head_x = curr_head_x
            new_head_y = curr_head_y - 1
        elif curr_head_direction == Direction.RIGHT:
            new_head_x = curr_head_x + 1
            new_head_y = curr_head_y
        elif curr_head_direction == Direction.DOWN:
            new_head_x = curr_head_x
            new_head_y = curr_head_y + 1
        elif curr_head_direction == Direction.LEFT:
            new_head_x = curr_head_x - 1
            new_head_y = curr_head_y
        else:
            print('No direction in head. Something went wrong. This should never print.')

        if self.is_snake_die(new_head_x, new_head_y):
            self.is_dead = True
            return

        self.insert_head((new_head_x, new_head_y, new_head_direction))

        if not self.is_eat_food():
            tail_x, tail_y = self.get_xy(self.get_tail())
            self.remove_tail()
            self.screen.reset_pixel_in_buffer(tail_x, tail_y)
        else:
            food_x, food_y = self.food
            self.screen.reset_pixel_in_buffer(food_x, food_y)
            self.food = self.create_food()
            food_x, food_y = self.food
            self.screen.set_pixel_in_buffer(food_x, food_y, Color(255, 0, 0, 255))


        self.screen.set_pixel_in_buffer(new_head_x, new_head_y, Color(255, 255, 255, 255))

        self.screen.update()

    def to_list(self):
        return self.body_list.to_list()

    def key_pressed(self, new_direction):
        x, y, curr_direction = self.get_head()

        if (curr_direction == Direction.DOWN and new_direction == Direction.UP
                or curr_direction == Direction.UP and new_direction == Direction.DOWN
                or curr_direction == Direction.LEFT and new_direction == Direction.RIGHT
                or curr_direction == Direction.RIGHT and new_direction == Direction.LEFT):
            return
        
        self.update_head((x, y, new_direction))
