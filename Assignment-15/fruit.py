import random
import arcade


class Fruit(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = random.randint(16, 500 - 16)
        self.center_y = random.randint(16, 500 - 16)
        self.change_x = 0
        self.change_y = 0


class Apple(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.pic = arcade.load_texture("apple.png")
        self.plus = 1

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(
            self.center_x, self.center_y, self.width, self.height, self.pic
        )


class Pear(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.pic = arcade.load_texture("pear.png")
        self.plus = 2

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(
            self.center_x, self.center_y, self.width, self.height, self.pic
        )


class Shit(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.pic = arcade.load_texture("shit.png")
        self.plus = -1

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(
            self.center_x, self.center_y, self.width, self.height, self.pic
        )
