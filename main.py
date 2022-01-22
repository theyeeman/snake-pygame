from os import DirEntry
import pygame
from Engine.snake import Snake
from Engine.screen import Screen
from Engine.direction import Direction
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    KEYUP,
)


def handle_events():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake.key_pressed(Direction.UP)
            elif event.key == K_RIGHT:
                snake.key_pressed(Direction.RIGHT)
            elif event.key == K_DOWN:
                snake.key_pressed(Direction.DOWN)
            elif event.key == K_LEFT:
                snake.key_pressed(Direction.LEFT)


if __name__ == "__main__":
    screen = Screen(50, 30, 20)
    screen.init_display()

    snake = Snake(screen)

    while not snake.is_dead:
        clock = pygame.time.Clock()
        screen.clear_screen()
        handle_events()
        screen.draw_snake(snake)
        snake.move_snake()
        clock.tick(10)
        
    pygame.quit()