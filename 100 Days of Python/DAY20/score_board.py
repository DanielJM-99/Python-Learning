from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")

    def score_on_board(self):
        self.goto(x=0, y=260)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 15, "normal"))

    def increment_score(self):
        self.clear()
        self.score += 1
