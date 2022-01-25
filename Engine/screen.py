from pygame import Color, display, draw, font

BACKGROUND_COLOR = Color(0, 0, 0, 255)
SNAKE_COLOR = Color(255, 255, 255, 255)
INFO_BAR_LINE_COLOR = Color(255, 255, 255, 255)
FOOD_COLOR = Color(255, 0, 0, 255)
TEXT_COLOR = Color(3, 232, 252, 255)


class Screen:
    def __init__(self, width, height, scale=10):
        self.width = width * scale
        self.height = height * scale
        self.scale = scale

        self.init_display()

    def init_display(self):
        display.init()
        font.init()
        self.surface = display.set_mode([self.width, self.height])
        display.set_caption('Barebones Snake')
        self.draw_info_bar_line()
        # self.clear_screen()
        # self.update()

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

    def draw_info_bar_line(self):
        draw.line(self.surface, INFO_BAR_LINE_COLOR, (0, self.scale-1), (self.width, self.scale-1), 1)

    def set_pixel_in_buffer(self, obj, color):
        self._draw_pixel(obj.x, obj.y, color)

    def reset_pixel_in_buffer(self, obj):
        self._draw_pixel(obj.x, obj.y, BACKGROUND_COLOR)

    def draw_init(self, snake):
        s = snake.to_list_full()

        for piece in s:
            self.set_pixel_in_buffer(piece, SNAKE_COLOR)

        self.set_pixel_in_buffer(snake.food, FOOD_COLOR)
        self.score_to_buffer(0)

        self.update()

    def clear_info_bar(self):
        draw.rect(self.surface, BACKGROUND_COLOR, (0, 0, self.width, self.scale))
        self.draw_info_bar_line()

    def score_to_buffer(self, score):
        self.clear_info_bar()
        self.text_to_buffer("Score: " + str(score), 0, 0, TEXT_COLOR)

    def text_to_buffer(self, text, x, y, color):
        rendered_text = font.SysFont('arial', self.scale - 1).render(str(text), True, color)
        self.surface.blit(rendered_text, (x, y))
        