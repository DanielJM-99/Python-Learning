import turtle as t
import time
from my_snake import Snake
from food import Food

screen = t.Screen()
screen.setup(width=600, height=600)
screen.clearscreen()
screen.tracer(0)

# 1 Create snake body: 3 turtle square objects
snake = Snake()

food = Food()

# Movement control 
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

    if (snake.head.distance(food) <= 30):
        food.create_food()


screen.exitonclick()
