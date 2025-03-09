import turtle as t
import random as rand

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(15)
t.colormode(255)

scr = t.Screen()

# Challenge 5: Draw a random walk, random color, thickness, faster

def change_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    return (r,g,b)

angles = [0, 90, 180, 270]

for _ in range(200):
    tim.color(change_color())
    tim.setheading(rand.choice(angles))
    tim.forward(25)
    
scr.exitonclick()
