from turtle import Turtle, Screen
import random 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
coordinates = [(-230, -100), (-230, -75), (-230, -50), (-230, -25), (-230, 0), (-230, 25)]
y_positions = [-70, -40, -10, 20, 50, 80]

# y_axis = -100
# turtles = []

# for t_col in colors:
#     new_turtle = Turtle("turtle")
#     new_turtle.color(t_col)
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=y_axis)
#     y_axis += 25

# for _ in range(len(colors)):
#     new_turtle = Turtle("turtle")
#     new_turtle.color(colors[_])
#     new_turtle.penup()
#     new_turtle.goto(coordinates[_])

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
