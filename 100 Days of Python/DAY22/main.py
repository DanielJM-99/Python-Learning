from turtle import Turtle, Screen
import time
from paddles import Paddle

#Create the screen
pong_screen = Screen()
pong_screen.setup(width=1000, height=500)
pong_screen.bgcolor("black")
pong_screen.tracer(0)
pong_screen.listen()

paddle = Paddle()

#Create paddle
# paddle.new_paddle()

game_is_on = True

while game_is_on:

    # Select heading
    pong_screen.onkey(paddle.move_up, "Up")
    pong_screen.onkey(paddle.move_down, "Down")

    # Update scree
    pong_screen.update()
    time.sleep(0.1)
    
    # Move paddle
    paddle.move()

pong_screen.exitonclick()
