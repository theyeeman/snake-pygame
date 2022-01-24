import pygame
import queue
from Engine.engine import Engine
from Engine.snake import Snake
from Engine.screen import Screen


if __name__ == "__main__":
    engine = Engine(40, 30, 20)

    while not engine.snake.is_dead:
        engine.clock.tick(12)
        engine.run_loop()
        
    pygame.quit()
