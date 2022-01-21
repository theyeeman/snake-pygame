import pygame
from Engine.snake import Snake
from Engine.screen import Screen

if __name__ == "__main__":
    screen = Screen(30, 30, 10)
    screen.init_display()

    snake = Snake(screen)

    while not snake.is_dead:
        clock = pygame.time.Clock()
        screen.clear_screen()
        screen.draw_snake(snake)
        snake.move_snake()
        clock.tick(20)
        
    pygame.quit()