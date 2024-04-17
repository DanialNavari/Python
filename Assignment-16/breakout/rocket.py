import arcade

class Racket(arcade.Sprite):
    def __init__(self, game):
        super().__init__("./images/paddle.png")
        self.width = 100
        self.height = 60
        self.center_x = game.width // 2
        self.center_y = 30
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.score = 0

    def move(self, width):
        if self.center_x <= 45:
            self.center_x = 45

        if self.center_x >= width - 45:
            self.center_x = width - 45

        self.center_x += self.change_x * self.speed
