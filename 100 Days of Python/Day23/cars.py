from turtle import Turtle
import random as r

CAR_COLORS = ["red", "green", "blue", "yellow", "black"]

class Cars():
    
    def __init__(self):
        self.list_of_cars = []
        self.speed = 5
        
    def create_cars(self):
        car = Turtle("square")
        car.color(r.choice(CAR_COLORS))
        car.shapesize(stretch_len=3, stretch_wid=1)
        car.penup()
        car.setheading(180)
        car.goto(x=280, y=r.randint(-250, 280))
        self.list_of_cars.append(car)        
        
    def move(self):
        for _ in range(len(self.list_of_cars)):
            self.list_of_cars[_].forward(self.speed)
            
    def next_level(self):
        self.speed += 5
        