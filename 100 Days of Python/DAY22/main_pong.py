from turtle import Turtle, Screen
import time 
from paddles import Paddles


# 1: Create screen
pong_screen = Screen()
pong_screen.setup(width=1000, height=600)
pong_screen.bgcolor("black")
pong_screen.tracer(0)



# 2: Create paddle
user_paddle = Paddles()

# Listen to user input
pong_screen.listen()
pong_screen.onkey(key="Up", fun=user_paddle.move_up)
pong_screen.onkey(key="Down", fun=user_paddle.move_down)

game_on = True
while game_on:
        # Screen update
        pong_screen.update()
        time.sleep(0.1)

        ## 2.1: Move paddle
        user_paddle.move_paddle()

pong_screen.exitonclick()
