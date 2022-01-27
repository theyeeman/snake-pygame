from Engine.engine import Engine

if __name__ == "__main__":
    engine = Engine(40, 30, 20)

    while not engine.start:
            engine.wait_for_start()

    while True:
        engine.prepare_to_start()

        while not engine.snake.is_dead:
            engine.clock.tick(15)
            engine.run_loop()

        engine.lose()

        while engine.snake.is_dead:
            engine.wait_for_retry()

        engine.reset()
