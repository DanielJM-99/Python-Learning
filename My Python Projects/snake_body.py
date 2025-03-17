import turtle as t
import time
from my_snake import Snake

screen = t.Screen()
screen.setup(width=500, height=500)
screen.tracer(0)

# 1 Create snake body: 3 turtle square objects
snake = Snake()

# Control movement
screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

snake_moving = True
while snake_moving:

    time.sleep(0.1)
    screen.update()
    
    # 2 Move the snake body
    snake.move()

screen.exitonclick()
