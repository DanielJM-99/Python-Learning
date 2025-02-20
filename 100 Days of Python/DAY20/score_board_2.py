from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align = ALIGNMENT, font= FONT)

    def increment_score(self):
        # Try to do all the code in the class instead of main
        self.score += 1
        self.clear()
        self.update_scoreboard()
