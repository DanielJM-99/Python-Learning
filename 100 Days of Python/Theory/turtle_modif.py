from turtle import Turtle, Screen
import random 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_axis = -100
all_turtles = []

for t_col in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(t_col)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    new_turtle.speed("fast")
    all_turtles.append(new_turtle)
    y_axis += 25

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0, 30)
        rand_head = random.randint(0, 20)
        turtle.setheading(rand_head)
        turtle.forward(rand_dist)

screen.exitonclick()
