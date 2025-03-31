from turtle import Turtle, Screen
import turtle
import random as ran
# Challege 1: Draw a 100 x 100 square
tim = Turtle()

# angle = 0
# for _ in range(4):
#     timmy.setheading(angle)
#     timmy.forward(100)
#     angle += 90    

# Challenge 2: Create a dashed line

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Challenge 3: Draw figures

# Triangle
# tim.sety(40)
# tim.speed("fastest")

# for sides in range(3, 11, 1):
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)

# CH3 Solut 2:

turtle.colormode(255)
 
def new_color():
    red = ran.randint(0, 255)
    green = ran.randint(0, 255)
    blue = ran.randint(0, 255)
    rgb = (red, green, blue)
    return rgb

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    tim.color(new_color())

n_screen = Screen()
n_screen.exitonclick()
