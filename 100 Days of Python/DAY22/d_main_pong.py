from turtle import Turtle, Screen
import time 
from d_paddles import Paddles
from d_ball import Ball
from d_scoreboard import Scoreboard

# 1: Create screen
pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.bgcolor("black")
pong_screen.tracer(0)

# 2: Create paddle
u_paddle = Paddles((350, 0))
c_paddle = Paddles((-350, 0))
ball = Ball()
score_board = Scoreboard()

# Listen to user input
pong_screen.listen()
pong_screen.onkeypress(key="Up", fun=u_paddle.move_up)
pong_screen.onkeypress(key="Down", fun=u_paddle.move_down)

pong_screen.onkeypress(key="w", fun=c_paddle.move_up)
pong_screen.onkeypress(key="s", fun=c_paddle.move_down)

game_on = True
while game_on:
        # Screen update
        time.sleep(0.1)
        pong_screen.update()
        ball.move_ball_r()
        print(ball.position())
        
        # Detect u_paddle
        if (ball.distance(u_paddle) < 50 and ball.xcor() > 320) or (ball.distance(c_paddle) < 50 and ball.xcor() < -320): 
                ball.increment_x *= -1.5
                
        # Detect ball out of bounds
        if ball.xcor() > 380:
                ball.reset_pos()
                score_board.l_score += 1
                score_board.update_score()
                
        if ball.xcor() < -380:
                ball.reset_pos()
                score_board.r_score += 1
                score_board.update_score()
                
pong_screen.exitonclick()
