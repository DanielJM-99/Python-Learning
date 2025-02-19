from turtle import Turtle, Screen
import random

# Random walk
# Random colors
# Thickness
# Painting speed 

def change_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

angles = [0, 90, 180, 270]

# Triangle
timmy = Turtle()
thickness = 10

for _ in range(100):
    timmy.speed(random.randint(1, 10))
    timmy.width(thickness + 5)
    timmy.color(change_colors())
    timmy.forward(30)
    timmy.right(random.choice(angles))

screen = Screen()
screen.exitonclick()