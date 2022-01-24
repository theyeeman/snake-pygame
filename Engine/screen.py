from pygame import Color, display, draw

BACKGROUND_COLOR = Color(0, 0, 0, 255)
SNAKE_COLOR = Color(255, 255, 255, 255)
FOOD_COLOR = Color(255, 0, 0, 255)

class Screen:
    def __init__(self, width, height, scale=10):
        self.width = width * scale
        self.height = height * scale
        self.scale = scale

        self.init_display()

    def init_display(self):
        display.init()
        self.surface = display.set_mode([self.width, self.height])
        self.clear_screen()
        self.update()

    def get_width(self):
        return self.width // self.scale

    def get_height(self):
        return self.height // self.scale

    def get_scale(self):
        return self.scale

    def clear_screen(self):
        self.surface.fill(BACKGROUND_COLOR)

    def update(self):
        display.flip()

    def destroy(self):
        display.quit()

    def _draw_pixel(self, x, y, colour):
        x_pos = x * self.scale
        y_pos = y * self.scale

        draw.rect(self.surface, colour, (x_pos, y_pos, self.scale, self.scale))

    def set_pixel_in_buffer(self, x, y, colour):
        self._draw_pixel(x, y, colour)

    def reset_pixel_in_buffer(self, x, y):
        self._draw_pixel(x, y, BACKGROUND_COLOR)

    def is_pixel_on(self, x, y):
        x_pos = x * self.scale
        y_pos = y * self.scale

        pixel_state = self.surface.get_at((x_pos, y_pos))

        if (pixel_state == BACKGROUND_COLOR):
            return False
        else:
            return True

    def draw_init(self, snake):
        s = snake.to_list()

        for piece in s:
            x, y, dir = piece
            self.set_pixel_in_buffer(x, y, SNAKE_COLOR)

        food_x, food_y = snake.food
        self.set_pixel_in_buffer(food_x, food_y, FOOD_COLOR)
        
        self.update()
