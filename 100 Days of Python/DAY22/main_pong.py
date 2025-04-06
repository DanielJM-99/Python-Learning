from turtle import Turtle, Screen
import time 
from paddles import Paddles

# 1: Create screen
pong_screen = Screen()
pong_screen.setup(width=1000, height=600)
pong_screen.bgcolor("black")
pong_screen.tracer(0)

# 2: Create paddle
paddles = Paddles()

# Listen to user input
pong_screen.listen()
pong_screen.onkeypress(key="Up", fun=paddles.move_up)
pong_screen.onkeypress(key="Down", fun=paddles.move_down)

game_on = True
while game_on:
        # Screen update
        pong_screen.update()
        time.sleep(0.08)
        
        # Move computer paddle
        paddles.move_computer()

pong_screen.exitonclick()
