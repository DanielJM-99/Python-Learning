from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def anti_clockwise():
    tim.setheading(tim.heading() + 10)
    
def clockwise():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.home()
    tim.clear()
        
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()