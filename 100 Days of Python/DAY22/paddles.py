from turtle import Turtle
COORDINATES = [(-480,0),(-480,20), (-480,40)]

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.squares = []

    def new_paddle(self):
        for location in COORDINATES:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(location)
            self.squares.append(new_square)
        self.squares[0].setheading(270)
    
    def move_up(self):
        self.squares[0].setheading(90)
    
    def move_down(self):
        self.squares[0].setheading(270)

    def move(self):
        for sq_num in range(len(self.squares)-1, 0, -1):
            sq_cor_x = self.squares[sq_num - 1].xcor()
            sq_cor_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(sq_cor_x, sq_cor_y)
        
        self.squares[0].forward(20)
