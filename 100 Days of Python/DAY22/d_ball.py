from turtle import Turtle
import random 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.increment_x = 10
        self.increment_y = 10

    def move_ball_r(self):
        #Detect wall colission    
        if self.ycor() > 280 or self.ycor() < -280:
            self.increment_y *= -1
            
        # Moves ball
        new_x = self.xcor() + self.increment_x
        new_y = self.ycor() + self.increment_y
        self.goto(new_x, new_y)
        
    def reset_pos(self):
        self.goto(0,0)
        self.increment_x /= 2
        self.increment_x *= -1
