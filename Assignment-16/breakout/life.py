import arcade

class Life(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__("./images/paddle.png")
        self.width = 25
        self.height = 25
        self.center_x = width
        self.center_y = height - 22
        self.change_x = 0
        self.change_y = 0
