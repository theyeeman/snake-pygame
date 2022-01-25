import pygame
from Engine.engine import Engine

if __name__ == "__main__":
    while True:
        engine = Engine(40, 30, 20)

        while not engine.start and not engine.snake.is_dead and not engine.quit:
            engine.wait_for_start()

        if not engine.quit:
            engine.prepare_to_start()

        while not engine.snake.is_dead and not engine.quit:
            engine.clock.tick(15)
            engine.run_loop()

        if not engine.quit:
            engine.lose()

        while engine.snake.is_dead and not engine.quit:
            engine.wait_for_retry()

        if engine.quit:
            break

    pygame.quit()
