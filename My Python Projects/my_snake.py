import turtle as t
from food import Food

POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]

class Snake(Food):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]
      
    def create_segments(self):
        for s_position in POSITIONS:
            self.extend_snake(s_position)

    def extend_snake(self, position):
        new_segment = t.Turtle("square")
        new_segment.color(self.change_color())
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

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
            