import pygame
from Engine.snake import Snake
from Engine.screen import Screen

if __name__ == "__main__":
    screen = Screen(20, 20, 10)
    screen.init_display()

    snake = Snake(screen)

    while not snake.is_dead:
        # run game
        pass

    pygame.quit()