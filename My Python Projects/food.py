import turtle
import random as r

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        new_food = turtle.Turtle("circle")
        new_food.color("blue")
        new_food.penup()
        x_axis = r.randint(-280, 280)
        y_axis = r.randint(-280, 280)
        new_food.goto(x=x_axis, y=y_axis)
