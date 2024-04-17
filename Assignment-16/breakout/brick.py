import arcade


class Brik(arcade.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.width = 35
        self.height = 20
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color
        )
