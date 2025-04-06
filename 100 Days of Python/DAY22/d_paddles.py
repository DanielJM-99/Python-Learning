from turtle import Turtle

UP = 90
DOWN = 270

class Paddles(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(start_pos)
        
    def move_up(self):
        if self.ycor() < 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -260:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
