import turtle as t
import time
from snake import Snake
from food import Food

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food.create_food()

snake_moving = True
while snake_moving:
    time.sleep(0.1)
    screen.update()

    snake.move()

screen.exitonclick()
