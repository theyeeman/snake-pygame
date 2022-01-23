import pygame
import queue
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
)

def store_events_in_queue(q):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            q.put(event)
            
            
def process_queue_event(q):
    try:
        event = q.get_nowait()

        if event.key == K_UP or event.key == K_w:
            print('up')
            snake.key_pressed(Direction.UP)
        elif event.key == K_RIGHT or event.key == K_d:
            print('right')
            snake.key_pressed(Direction.RIGHT)
        elif event.key == K_DOWN or event.key == K_s:
            print('down')
            snake.key_pressed(Direction.DOWN)
        elif event.key == K_LEFT or event.key == K_a:
            print('left')
            snake.key_pressed(Direction.LEFT)
    except queue.Empty:
        return


if __name__ == "__main__":
    event_queue = queue.SimpleQueue()

    screen = Screen(40, 30, 20)

    snake = Snake(screen)
    screen.draw_snake_init(snake)
    clock = pygame.time.Clock()

    while not snake.is_dead:
        clock.tick(12)
        store_events_in_queue(event_queue)
        process_queue_event(event_queue)
        snake.move_snake()
        
    pygame.quit()
