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

        self.head = self.segments[0]
         
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            coordinates = self.segments[segment - 1].position()
            self.segments[segment].goto(coordinates)

        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:  
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)
        
    def right(self):
        if self.head.heading() == 180:
            pass 
        else:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180) 
            