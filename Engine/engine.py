import queue
import pygame
from Engine.snake import Snake
from Engine.direction import Direction
from Engine.screen import Screen
from pygame.color import Color
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_s,
    K_a,
    K_d,
    KEYDOWN,
)


class Engine():
    def __init__(self, width, height, scale):
        self.screen = Screen(width, height, scale)
        self.snake = Snake(self.screen)
        self.event_queue = queue.SimpleQueue()
        self.clock = pygame.time.Clock()
        self.valid_keys = set(
            (
                K_UP,
                K_DOWN,
                K_LEFT,
                K_RIGHT,
                K_w,
                K_s,
                K_a,
                K_d,
            )
        )

        self.screen.draw_init(self.snake)

    def store_events_in_queue(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.valid_keys:
                    self.event_queue.put(event)

    def process_queue_event(self):
        try:
            event = self.event_queue.get_nowait()

            if event.key == K_UP or event.key == K_w:
                self.key_pressed(Direction.UP)
            elif event.key == K_RIGHT or event.key == K_d:
                self.key_pressed(Direction.RIGHT)
            elif event.key == K_DOWN or event.key == K_s:
                self.key_pressed(Direction.DOWN)
            elif event.key == K_LEFT or event.key == K_a:
                self.key_pressed(Direction.LEFT)
        except queue.Empty:
            return

    def key_pressed(self, new_direction):
        x, y, curr_direction = self.snake.get_head()

        if (curr_direction == Direction.DOWN and new_direction == Direction.UP
                or curr_direction == Direction.UP and new_direction == Direction.DOWN
                or curr_direction == Direction.LEFT and new_direction == Direction.RIGHT
                or curr_direction == Direction.RIGHT and new_direction == Direction.LEFT):
            return
        
        self.snake.update_head((x, y, new_direction))

    def draw_screen(self):
        pass

    def next_frame(self):
        curr_head_x, curr_head_y, curr_head_direction = self.snake.get_head()
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

        if self.snake.is_snake_die(new_head_x, new_head_y):
            self.snake.is_dead = True
            return

        self.snake.insert_head((new_head_x, new_head_y, new_head_direction))

        if not self.snake.is_eat_food():
            tail_x, tail_y = self.snake.get_xy(self.snake.get_tail())
            self.snake.remove_tail()
            self.screen.reset_pixel_in_buffer(tail_x, tail_y)
        else:         
            self.snake.food = self.snake.create_food()
            self.screen.set_pixel_in_buffer(self.snake.food[0], self.snake.food[1], Color(255, 0, 0, 255))
        
        self.screen.set_pixel_in_buffer(new_head_x, new_head_y, Color(255, 255, 255, 255))
        self.screen.update()

    def run_loop(self):
        self.store_events_in_queue()
        self.process_queue_event()
        self.next_frame()