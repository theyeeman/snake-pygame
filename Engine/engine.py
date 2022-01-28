import pygame
from pygame.locals import K_RETURN, KEYDOWN
from Engine.snake import Snake, Position
from Engine.screen import Screen, SNAKE_COLOR, FOOD_COLOR
from Engine.eventhandler import EventHandler


class Engine():
    def __init__(self, width, height, scale):
        pygame.init()
        self.start = False
        self.screen = Screen(width, height, scale)
        self.snake = Snake(self.screen)
        self.event_handler = EventHandler(self.snake)
        self.empty_set = self.generate_empty_set()
        self.food = self.create_food()
        self.clock = pygame.time.Clock()

        self.screen.draw_wait_init()

    def generate_empty_set(self):
        s = set()

        for i in range(self.screen.get_width()):
            for j in range(1, self.screen.get_height()):  # Top row reserved for info bar
                s.add(Position(i, j))

        s.discard(self.snake.get_head())

        return s

    def create_food(self):
        food = self.empty_set.pop()
        self.empty_set.add(food)  # food position is still considered and empty spot

        return food

    def is_eat_food(self):
        if self.snake.get_head() == self.food:
            return True

        return False

    def is_snake_die(self, next_head):
        if next_head in self.empty_set:
            return False
        
        return True

    def next_frame(self):
        next_head = self.snake.get_next_head()

        if self.is_snake_die(next_head):
            self.snake.is_dead = True
            return

        self.snake.insert_head(next_head)
        self.empty_set.discard(next_head)
        self.screen.set_pixel_in_buffer(next_head, SNAKE_COLOR)

        if not self.is_eat_food():
            tail = self.snake.get_tail()
            self.snake.remove_tail()
            self.empty_set.add(tail)
            self.screen.reset_pixel_in_buffer(tail)
        else:
            self.snake.score += 1
            self.food = self.create_food()
            self.screen.set_pixel_in_buffer(self.food, FOOD_COLOR)
            self.screen.score_to_buffer(self.snake.score)

        self.screen.update()

    def run_loop(self):
        self.event_handler.store_events()
        self.event_handler.process_queue_event()
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
        self.screen.draw_start_init(self.snake, self.food)

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
        self.event_handler = EventHandler(self.snake)
        self.empty_set = self.generate_empty_set()
