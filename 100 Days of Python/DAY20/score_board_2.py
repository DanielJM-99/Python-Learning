from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        # Read high score from data
        with open(r"C:\Users\T03USOH\OneDrive - NEW YORK LIFE INSURANCE COMPANY\Documents\Python-Learning\100 Days of Python\DAY20\data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align = ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Write into high score
            with open(r"C:\Users\T03USOH\OneDrive - NEW YORK LIFE INSURANCE COMPANY\Documents\Python-Learning\100 Days of Python\DAY20\data.txt", mode="w") as file:
                #file.write(str(self.score))
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(x=0, y=0)
    #    self.write("GAME OVER", align = ALIGNMENT, font= FONT)

    def increment_score(self):
        # Try to do all the code in the class instead of main
        self.score += 1
        self.update_scoreboard()
