import turtle
import random as r

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def change_color(self):
        self.red = r.uniform(0, 1)
        self.green = r.uniform(0, 1)
        self.blue = r.uniform(0, 1)
        self.new_color = (self.red, self.green, self.blue)
        return (self.new_color)

    def create_food(self):
        self.showturtle()
        self.shape("turtle")
        self.color(self.change_color())
        self.shapesize(0.8, 0.8)
        self.penup()
        x_axis = r.randint(-280, 280)
        y_axis = r.randint(-280, 280)
        self.goto(x=x_axis, y=y_axis)
