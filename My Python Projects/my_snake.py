import turtle as t

class Snake:
    def __init__(self):
        self.segments = []
        x_axis = [20, 40, 60]
        for _ in range(3):
            new_segment = t.Turtle("square")
            new_segment.color("black")
            new_segment.penup()
            new_segment.goto(x_axis[_], y=0)
            self.segments.append(new_segment)
         
    def up(self):
        self.segments[0].setheading(90)
    
    def down(self):
        self.segments[0].setheading(270)
    
    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            coordinates = self.segments[segment - 1].position()
            self.segments[segment].goto(coordinates)

        self.segments[0].forward(20)
