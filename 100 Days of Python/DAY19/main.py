from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear_drawing():
    tim.home()
    tim.clear()
    
screen.listen()

# When usign a function as an argument, we dont add parenthesis at the end
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clear_drawing)

screen.exitonclick()