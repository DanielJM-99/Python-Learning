from turtle import Turtle

STARTING_POS = (0,-280)

class User(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.move_to_beginning()
        
    def move(self):
        self.forward(10)
        
    def move_to_beginning(self):
        self.goto(STARTING_POS)
        