from pygame import Color, display, draw

PIXEL_OFF = Color(0, 0, 0, 255)
PIXEL_ON = Color(255, 255, 255, 255)

class Screen:
    def __init__(self, width, height, scale=10):
        self.width = width * scale
        self.height = height * scale
        self.scale = scale

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
        self.surface.fill(PIXEL_OFF)

    def update(self):
        display.flip()

    def destroy(self):
        display.quit()

    def _draw_pixel(self, x, y, colour):
        x_pos = x * self.scale
        y_pos = y * self.scale

        draw.rect(self.surface, colour, (x_pos, y_pos, self.scale, self.scale))

    def set_pixel_in_buffer(self, x, y):
        self._draw_pixel(x, y, PIXEL_ON)

    def reset_pixel_in_buffer(self, x, y):
        self._draw_pixel(x, y, PIXEL_OFF)

    def is_pixel_on(self, x, y):
        x_pos = x * self.scale
        y_pos = y * self.scale

        pixel_state = self.surface.get_at((x_pos, y_pos))

        if (pixel_state == PIXEL_OFF):
            return False
        else:
            return True

    def draw_snake(self, snake):
        s = snake.to_list()

        for piece in s:
            x, y, dir = piece
            self.set_pixel_in_buffer(x, y)

        self.update()
