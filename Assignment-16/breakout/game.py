import random
import arcade
from brick import Brik
from rocket import Racket
from ball import Ball
from life import Life


class Game(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Breakout GAME 🧱⚾", center_window=True)
        self.background = arcade.load_texture("./images/background.png")
        self.game_over = arcade.load_texture("./images/game over.png")
        self.win = arcade.load_texture("./images/win.png")
        self.mode = None
        self.rocket = Racket(self)
        self.ball = Ball(self.rocket)
        self.ball_mode = "stay"
        self.color = [
            arcade.color.BLUE,
            arcade.color.ORANGE,
            arcade.color.RED,
            arcade.color.ORANGE,
            arcade.color.PURPLE,
            arcade.color.GRAY,
        ]
        self.brik_list = []
        self.life_list = []

        for x in range(230, self.width - 200, 48):
            i = 0
            for y in range(self.height - 220, self.height - 75, 25):
                color = self.color[i]
                new_brik = Brik(x, y, color)
                self.brik_list.append(new_brik)
                i += 1

        for i in range(self.width - 20, self.width - 80, -25):
            new_life = Life(i, self.height)
            self.life_list.append(new_life)

    def on_draw(self):
        arcade.start_render()

        score_text = f" Score : {self.rocket.score}"

        if self.mode == "game_over":
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(
                0, 0, self.width, self.height, self.game_over
            )
            """ arcade.draw_text(
                score_text, (self.width // 2) - 100, 50, arcade.color.DARK_PINK, 30
            ) """

        elif self.mode == "win":
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.win)
            arcade.draw_text(score_text, 20, 30, arcade.color.RED, 30)

        else:
            arcade.set_background_color(arcade.color.SILVER)
            arcade.draw_lrwh_rectangle_textured(
                5, 5, self.width - 10, self.height - 50, self.background
            )
            arcade.draw_rectangle_outline(
                self.width // 2,
                self.height - 22,
                self.width - 10,
                36,
                arcade.color.BLACK,
                2,
            )
            self.rocket.draw()
            self.ball.draw()

            for brik in self.brik_list:
                brik.draw()

            for life in self.life_list:
                life.draw()

            arcade.draw_text(score_text, 10, self.height - 30, arcade.color.BLACK, 20)

        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        self.rocket.center_x = x

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.rocket.change_x = 1

        if symbol == arcade.key.LEFT:
            self.rocket.change_x = -1

        if symbol == arcade.key.SPACE:
            self.ball.change_y = 1
            self.ball.change_x = random.choice([1, -1])
            self.ball_mode = "move"

    def on_key_release(self, symbol, modifiers):
        self.rocket.change_x = 0

    def on_update(self, delta_time):
        self.rocket.move(self.width)
        self.ball.move(self.width, self.ball_mode)

        if self.ball_mode == "stay":
            self.ball.center_x = self.rocket.center_x

        if self.ball.center_x < 220 or self.ball.center_x > self.width - 210:
            self.ball.change_x *= -1

        if self.ball.center_y > self.height - 55:
            self.ball.change_y *= -1

        if arcade.check_for_collision(self.ball, self.rocket):
            self.ball.change_y *= -1

        for brik in self.brik_list:
            if arcade.check_for_collision(self.ball, brik):
                self.brik_list.remove(brik)
                self.rocket.score += 1
                self.ball.speed += 0.1
                self.rocket.speed += 0.05

                if self.ball.center_y - 20 < brik.center_y < self.ball.center_y + 20:
                    self.ball.change_y *= -1

                if self.ball.center_x - 30 < brik.center_x < self.ball.center_x + 30:
                    self.ball.change_x *= -1

        if self.ball.center_y < 25:
            self.rocket.score -= 1
            self.life_list.pop()
            del self.ball
            self.ball = Ball(self.rocket)
            self.ball_mode = "stay"

        if len(self.life_list) == 0:
            self.mode = "game_over"

        if len(self.brik_list) == 0:
            self.mode = "win"


game = Game()
arcade.run()
