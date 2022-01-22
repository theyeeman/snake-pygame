import pygame
from Engine.snake import Snake
from Engine.screen import Screen
from Engine.direction import Direction
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
    KEYUP,
)


def handle_events():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                snake.key_pressed(Direction.UP)
            elif event.key == K_RIGHT or event.key == K_d:
                snake.key_pressed(Direction.RIGHT)
            elif event.key == K_DOWN or event.key == K_s:
                snake.key_pressed(Direction.DOWN)
            elif event.key == K_LEFT or event.key == K_a:
                snake.key_pressed(Direction.LEFT)
            break

if __name__ == "__main__":
    screen = Screen(40, 30, 20)
    screen.init_display()

    snake = Snake(screen)
    
    while not snake.is_dead:
        clock = pygame.time.Clock()
        screen.clear_screen()
        handle_events()
        screen.draw_snake(snake)
        snake.move_snake()
        clock.tick(15)

    pygame.quit()
