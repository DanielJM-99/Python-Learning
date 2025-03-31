from turtle import Turtle, Screen
import turtle
import random as rand

COORDINATES = [(-360, -200), (-360, -150), (-360,-100), (-360, -50), (-360, 0)]
COLORS = ["green", "red", "blue", "black", "orange"]

screen = Screen()
title = Turtle()
title.hideturtle()

user_guess = screen.textinput("Turtle Race", "Which turtle do you think will win?")

# Create turtles
turtles = []
for _ in range(5):
    new_turtle = Turtle("turtle")
    new_turtle.speed("fastest")
    new_turtle.color(COLORS[_])
    turtles.append(new_turtle)

# Move turtles starting position
for _ in range(5):
    turtles[_].penup()
    turtles[_].goto(COORDINATES[_])
    
still_running = True
while still_running:
    for _ in range(len(COORDINATES)):
        turtles[_].forward(rand.randint(0, 20))
        if turtles[_].xcor() >= 360:
            winner = turtles[_].color()[0]
            if winner == user_guess:
                title.write("You win!", align="center", font=('Arial', 20, 'normal'))
            else:
                title.write("You lose!", align="center", font=('Arial', 20, 'normal'))
            still_running = False

screen.exitonclick()
