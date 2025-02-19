#from turtle import Turtle, Screen, turtle
import turtle as t
import random

def change_colors():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

# tim = Turtle()
# tim.shape("turtle")
# tim.color("#0000FF")

# First challenge
#for times in range(4):
#    tim.forward(100)
#    tim.right(90)

# Second challenge
#for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

# Third challenge

#def draw_shape(number_of_sides):
    shape.color(change_colors())
    for _ in range(number_of_sides):
        shape.forward(100)
        shape.right((360/number_of_sides))

# Triangle
#shape = Turtle()
#shape.sety(50)

# for sides in range(3, 11):
    #draw_shape(sides)

# Fourth challenge

tim = t.Turtle()

#directions = [0, 90, 180, 270]
#tim.pensize(15)
#tim.speed("fastest")

#for _ in range(200):
#    tim.color(change_colors())
#    tim.forward(30)
#    tim.setheading(random.choice(directions))

# Tuples

my_tuple = (1, 3, 8)
print(my_tuple[2])

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# screen = Screen()
# screen.exitonclick()
