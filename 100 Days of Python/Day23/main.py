#Break down the problem

# 1: Create game screen
# 2: Create player/user turtle 
## 2.1 : Move turtle to startig pos
## 2.2 : Make turtle move only forward with Up key
# 3: Generate random car objects (turtle 3 x 1)
## 3.1: Make cars move from left to right (10)
## 3.12: Assign random color to cars
## 3.2: Detect collision of any car with turtle and stop game
# 4: Create score and levels of game (everytime turtle goes over y screen
## turtle goes back to origin and cars move faster)
## Update Score 

from turtle import Turtle, Screen
import time
from user import User
from cars import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = User()
cars = Cars()
screen.listen()
screen.onkey(fun=player.move, key="Up")
        
game_on = True
while game_on:
    time.sleep(0.1)
    cars.move()
    screen.update()

screen.exitonclick()
