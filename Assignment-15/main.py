import random
from typing import Optional
import arcade
from arcade import Texture

from fruit import Apple
from fruit import Pear
from fruit import Shit
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake 🐍")
        arcade.set_background_color(arcade.color.KHAKI)

        self.food = Apple(self)
        self.shit = Shit(self)
        self.pear = Pear(self)
        self.snake = Snake(self)
        self.black_page = arcade.load_texture("black.png")
        self.gameover = arcade.load_sound(":resources:sounds/gameover3.wav", False)
        self.state = 1

    def del_all(self):
        del self.food
        del self.pear
        del self.shit
        self.food = Apple(self)
        self.shit = Shit(self)
        self.pear = Pear(self)

    def on_draw(self):
        arcade.start_render()

        self.food.draw()
        self.pear.draw()
        self.shit.draw()
        self.snake.draw()

        arcade.draw_text(
            str("Score: " + str(self.snake.score)),
            self.width / 2,
            15,
            arcade.color.WHITE,
            18,
        )

        if self.state == 0:
            arcade.draw_lrtb_rectangle_filled(
                0, self.width, self.height, 0, arcade.color.BLACK
            )
            arcade.draw_text(
                "GAME OVER!", self.width // 6, self.height // 2, arcade.color.WHITE, 40
            )

        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.score += 1
            self.del_all()
        elif arcade.check_for_collision(self.snake, self.pear):
            self.snake.score += 2
            self.del_all()
            
        elif arcade.check_for_collision(self.snake, self.shit):  
            self.snake.score -= 1
            self.del_all()
        
        if (
            self.snake.center_x < 0
            or self.snake.center_x > 500
            or self.snake.center_y < 0
            or self.snake.center_y > self.height
            or self.snake.score < 0
        ):
            self.state = 0


if __name__ == "__main__":
    game = Game()
    arcade.run()
