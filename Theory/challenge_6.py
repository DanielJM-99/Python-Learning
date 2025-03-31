import turtle as t
import random as rand

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
scr = t.Screen()

# Challenge 6: Make a spirograph that changes color and stop on angle 360.

def change_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    return (r,g,b)

# def spirograph(num_circles):
    
#     new_angle = 0
#     angle = 360 / num_circles

#     for _ in range(num_circles):   
#         new_angle += angle
#         tim.circle(100)
#         tim.setheading(new_angle)
#         tim.color(change_color())

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.circle(100)
        tim.color(change_color())
        tim.setheading(tim.heading() + gap_size)
    
draw_spirograph(10)
    
    
scr.exitonclick()