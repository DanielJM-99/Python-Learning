from turtle import Turtle

class User(Turtle):
    
    def __init__(self, ):
        super().__init__()
    
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)
    
    def move(self):
        self.forward(10)
    