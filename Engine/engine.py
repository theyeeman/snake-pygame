import queue
import pygame
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
from Engine.snake import Snake, Position
from Engine.direction import Direction
from Engine.screen import Screen
from Engine.screen import SNAKE_COLOR, FOOD_COLOR


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

    def store_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.valid_keys:
                    self.event_queue.put(event)

            elif event.type == pygame.QUIT:
                self.snake.is_dead = True

    def process_queue_event(self):
        try:
            event = self.event_queue.get_nowait()

            if event.key == K_UP or event.key == K_w:
                self.process_key_press(Direction.UP)
            elif event.key == K_RIGHT or event.key == K_d:
                self.process_key_press(Direction.RIGHT)
            elif event.key == K_DOWN or event.key == K_s:
                self.process_key_press(Direction.DOWN)
            elif event.key == K_LEFT or event.key == K_a:
                self.process_key_press(Direction.LEFT)
        except queue.Empty:
            return

    def process_key_press(self, new_direction):
        head = self.snake.get_head()

        if (head.direction == Direction.DOWN and new_direction == Direction.UP
                or head.direction == Direction.UP and new_direction == Direction.DOWN
                or head.direction == Direction.LEFT and new_direction == Direction.RIGHT
                or head.direction == Direction.RIGHT and new_direction == Direction.LEFT):
            return

        self.snake.overwrite_head(Position(head.x, head.y, new_direction))

    def next_frame(self):
        next_head = self.snake.get_next_head()

        if self.snake.is_snake_die(next_head):
            self.snake.is_dead = True
            return

        self.snake.insert_head(next_head)
        self.screen.set_pixel_in_buffer(next_head, SNAKE_COLOR)

        if not self.snake.is_eat_food():
            tail = self.snake.get_tail()
            self.snake.remove_tail()
            self.screen.reset_pixel_in_buffer(tail)
        else:
            self.snake.food = self.snake.create_food()
            self.screen.set_pixel_in_buffer(self.snake.food, FOOD_COLOR)

        self.screen.update()

    def run_loop(self):
        self.store_events()
        self.process_queue_event()
        self.next_frame()
