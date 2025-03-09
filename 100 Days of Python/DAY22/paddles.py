from turtle import Turtle
COORDINATES = [(-480,0),(-480,20), (-480,40)]
HEADING = [90, 270]

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.squares = []
        self.new_paddle()
        self.head = self.squares[0]
        self.head.setheading(HEADING[0])

    def new_paddle(self):
        for location in COORDINATES:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(location)
            self.squares.append(new_square)
    
    def move_up(self):
        self.head.setheading(HEADING[0])
    
    def move_down(self):
        self.head.setheading(HEADING[1])

    def move(self):
        for sq_num in range(len(self.squares)-1, 0, -1):
            sq_cor_x = self.squares[sq_num - 1].xcor()
            sq_cor_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(sq_cor_x, sq_cor_y)
        self.head.forward(20)
