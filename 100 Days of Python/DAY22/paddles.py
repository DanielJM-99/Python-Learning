from turtle import Turtle
import random as r

U_POSITIONS = [(-480, 0), (-480, 20), (-480, 40), (-480, 60)]
C_POSITIONS = [(480, 0), (480, 20), (480, 40), (480, 60)]
UP = 90
DOWN = 270

up_or_down = [UP, DOWN]

class Paddles(Turtle):

    def __init__(self):
        super().__init__()
        # Paddle segments
        self.paddle_segments_user = []
        self.paddle_segments_computer = []
        self.create_paddle(U_POSITIONS, self.paddle_segments_user)
        self.create_paddle(C_POSITIONS, self.paddle_segments_computer)
    
    def create_paddle(self, coordiantes, pd_segments):
        for starting_position in coordiantes:
            pd_seg = Turtle("square")
            pd_seg.color("white")
            pd_seg.penup()
            pd_seg.goto(starting_position)
            pd_segments.append(pd_seg)

    def move_paddle(self, direction):
        for segment in range(len(self.paddle_segments_user)):
            self.paddle_segments_user[segment].setheading(direction)
            self.paddle_segments_user[segment].forward(20)
            
    def move_up(self):
        # Head upwards
        if self.paddle_segments_user[-1].ycor() < 280:
            self.move_paddle(UP)

    def move_down(self):
        # Head downwards
        if self.paddle_segments_user[0].ycor() > -280:
            self.move_paddle(DOWN)
            
    def move_computer(self):
        for segment in range(len(self.paddle_segments_computer)):
            if self.paddle_segments_computer[0].ycor() > -280:
                self.paddle_segments_computer[segment].setheading(DOWN)  
                print(self.paddle_segments_computer[0].ycor()) 
            else:
                self.paddle_segments_computer[segment].setheading(UP)
                    
            self.paddle_segments_computer[segment].forward(20)
            
