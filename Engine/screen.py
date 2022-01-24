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
        display.set_caption('Barebones Snake')
        self.clear_screen()
        self.update()

    def get_width(self):
        return self.width // self.scale

    def get_height(self):
        return self.height // self.scale

    def clear_screen(self):
        self.surface.fill(BACKGROUND_COLOR)

    def update(self):
        display.flip()

    def _draw_pixel(self, x, y, colour):
        x_pos = x * self.scale
        y_pos = y * self.scale

        draw.rect(self.surface, colour, (x_pos, y_pos, self.scale, self.scale))

    def set_pixel_in_buffer(self, obj, color):
        self._draw_pixel(obj.x, obj.y, color)

    def reset_pixel_in_buffer(self, obj):
        self._draw_pixel(obj.x, obj.y, BACKGROUND_COLOR)

    def draw_init(self, snake):
        s = snake.to_list_full()

        for piece in s:
            self.set_pixel_in_buffer(piece, SNAKE_COLOR)

        self.set_pixel_in_buffer(snake.food, FOOD_COLOR)

        self.update()
