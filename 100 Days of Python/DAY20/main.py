from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game.")

# Challenge 1: Create 3 turtles and position them like so, each should be a white square def size 20 x 20
x_axis = 0

for _ in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.setx(x_axis)
    x_axis -= 20
    
screen.exitonclick()

# Challenge 1: Create 3 turtles and position them like so, each should be a white square def size 20 x 20

# segment_1 = Turtle(shape="square")
# segment_1.color("white")

# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(x=-20, y=0)

# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(x=-40, y=0)

### ----

# starting_positions = [(0,0), (-20,0), (-40,0)]

# segments = []

# # Created objects for snake body
# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
