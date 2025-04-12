from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(x=-260, y=260)
        self.write(f"LEVEL: {self.score}", move=False, font=("Arial", 15, "normal"))
        self.score += 1
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, font=("Arial", 15, "normal"), align="center")
        