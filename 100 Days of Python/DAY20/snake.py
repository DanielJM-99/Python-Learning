from turtle import Turtle

class Snake:

    def __init__(self):
        starting_positions = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        # Created objects for snake body
        for position in starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def move(self):
        # created loop to move snake body, segments following head
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)
    
    def left(self):
        self.segments[0].setheading(180)
    
    def right(self):
        self.segments[0].setheading(0)
        