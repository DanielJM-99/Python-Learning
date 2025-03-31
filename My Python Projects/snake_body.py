import turtle as t
import time
from my_snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.clearscreen()
screen.tracer(0)

# 1 Create snake body: 3 turtle square objects
snake = Snake()
food = Food()
food.create_food()
score_b = Scoreboard()

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

    # Detect colission with food
    if abs(snake.head.xcor()- food.xcor()) < 10 and  abs(snake.head.ycor()- food.ycor()) < 10:  # Can be changes with distance method
        food.create_food()
        snake.extend_snake(snake.segments[-1].position())
        score_b.add_score()

    # Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_b.game_over()
        snake_moving = False

    # Colission with tail
    for segment in snake.segments[1:]:
          if snake.head.distance(segment) < 5:
               score_b.game_over()
               snake_moving = False

screen.exitonclick()
