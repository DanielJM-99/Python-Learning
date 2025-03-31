from turtle import Turtle

POSITIONS = [(-480, 0), (-480, 20), (-480, 40), (-480, 60)]
UP = 90
DOWN = 270

class Paddles(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_segments = []
        self.create_paddle()
        self.paddle_segments[0].setheading(DOWN)
    
    def create_paddle(self):
        for starting_position in POSITIONS:
            pd_seg = Turtle("square")
            pd_seg.color("white")
            pd_seg.penup()
            pd_seg.goto(starting_position)
            self.paddle_segments.append(pd_seg)

    def move_paddle(self):
        for segment in range(len(self.paddle_segments)- 1, 0, -1):
            new_pos = self.paddle_segments[segment - 1].position()
            self.paddle_segments[segment].goto(new_pos)
        self.paddle_segments[0].forward(20)

    def move_up(self):
        self.paddle_segments[0].setheading(UP)

    def move_down(self):
        self.paddle_segments[0].setheading(DOWN)

