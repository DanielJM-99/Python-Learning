from turtle import Screen
from a_padle import Paddle
from a_ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
# Controls for right paddle
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
# Controls for left paddle
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

screen.exitonclick()
