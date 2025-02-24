from turtle import Screen
import time
from snake_2 import Snake
from food import Food
from score_board_2 import Score

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:

    # Used methods to update when movement is complete
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect colission with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increment_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        game_is_on = False

    # Detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
