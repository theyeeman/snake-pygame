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
    K_RETURN,
    KEYDOWN,
)
from Engine.snake import Snake, Position
from Engine.direction import Direction
from Engine.screen import Screen, SNAKE_COLOR, FOOD_COLOR, BACKGROUND_COLOR, TEXT_COLOR


class Engine():
    def __init__(self, width, height, scale):
        pygame.init()
        self.start = False
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

        self.screen.draw_wait_init()

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
            self.snake.score += 1
            self.snake.food = self.snake.create_food()
            self.screen.set_pixel_in_buffer(self.snake.food, FOOD_COLOR)
            self.screen.score_to_buffer(self.snake.score)

        self.screen.update()

    def run_loop(self):
        self.store_events()
        self.process_queue_event()
        self.next_frame()

    def wait_for_start(self):
        event = pygame.event.poll()

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.start = True

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def prepare_to_start(self):
        self.screen.draw_start_init(self.snake)

    def lose(self):
        self.screen.draw_lose_text()

    def wait_for_retry(self):
        event = pygame.event.poll()

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.snake.is_dead = False

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def reset(self):
        self.start = False
        self.snake = Snake(self.screen)
        self.event_queue = queue.SimpleQueue()
