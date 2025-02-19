from turtle import Turtle, Screen
import random

def change_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

shape = Turtle()
shape.speed("fastest")
angle = 0

for _ in range(100):
    shape.circle(100)
    shape.setheading(angle)
    shape.color(change_color())
    angle += 5

screen = Screen()
screen.exitonclick()