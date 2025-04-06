from turtle import Turtle
import random 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed_x = 10
        self.speed_y = 5

    def move_ball_r(self):
        if self.xcor() >= 380 or self.xcor() <= -380  or self.ycor() >= 280 or self.ycor() <= -280:
            self.speed_x *= -1
            self.speed_y *= -1
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y
        self.goto(new_x, new_y)


