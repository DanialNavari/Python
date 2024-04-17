
import arcade

class Ball ( arcade.Sprite ) :

    def __init__ ( self , racket ) :
        super().__init__("./images/ball.png")
        self.width = 22
        self.height = 22
        self.angle = -45
        self.center_x = racket.center_x
        self.center_y = racket.center_y + 10
        self.change_x = 0
        self.change_y = 0
        self.speed = 3


    def move ( self , width , mode ) :
        if mode == "stay" :
            if self.center_x <= 45 :
                self.center_x = 45
            
            if self.center_x >= width - 45 :
                self.center_x = width - 45
                
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed