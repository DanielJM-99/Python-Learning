from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = -1
        self.add_score()
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.goto(x=0, y=250)
        self.write(f"Score = {self.score}", align="center", font=("Arial", 14, "bold"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Arial", 14, "bold"))

