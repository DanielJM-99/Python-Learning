from turtle import Turtle, Screen
import time 
from d_paddles import Paddles
from d_ball import Ball

# 1: Create screen
pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.bgcolor("black")
pong_screen.tracer(0)

# 2: Create paddle
u_paddle = Paddles((350, 0))
c_paddle = Paddles((-350, 0))
ball = Ball()

# Listen to user input
pong_screen.listen()
pong_screen.onkeypress(key="Up", fun=u_paddle.move_up)
pong_screen.onkeypress(key="Down", fun=u_paddle.move_down)

pong_screen.onkeypress(key="w", fun=c_paddle.move_up)
pong_screen.onkeypress(key="s", fun=c_paddle.move_down)

game_on = True
while game_on:
        # Screen update
        pong_screen.update()
        time.sleep(0.1)
        ball.move_ball_r()
        
pong_screen.exitonclick()
