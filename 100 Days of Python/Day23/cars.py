from turtle import Turtle
import random as r

class Cars():
    
    def __init__(self):
        self.cars = []
        self.create_cars()
        
    def create_cars(self):
        for _ in range(5):
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(x=280, y=r.randint(-250, 280))
            self.cars.append(new_car)         
        
    def move(self):
        for _ in range(len(self.cars)):
            self.cars[_].forward(10)