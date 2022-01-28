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
from Engine.direction import Direction
from Engine.snake import Position

class EventHandler():
    def __init__(self, snake):
        self.event_queue = queue.SimpleQueue()
        self.snake = snake
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

    def store_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.valid_keys:
                    self.event_queue.put(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

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