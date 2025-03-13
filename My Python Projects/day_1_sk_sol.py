import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

snake_moving = True
while snake_moving:
    time.sleep(0.10)
    screen.update()

    snake.move()

screen.exitonclick()
