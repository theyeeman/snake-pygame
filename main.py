import pygame
from Engine.engine import Engine

if __name__ == "__main__":
    engine = Engine(40, 30, 20)

    while not engine.snake.is_dead:
        engine.clock.tick(15)
        engine.run_loop()

    pygame.quit()
