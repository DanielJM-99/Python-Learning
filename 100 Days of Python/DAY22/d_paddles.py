from turtle import Turtle

U_POSITIONS = [(-480, 0), (-480, 20), (-480, 40), (-480, 60)]
C_POSITIONS = [(480, 0), (480, 20), (480, 40), (480, 60)]
UP = 90
DOWN = 270

class Paddles(Turtle):

    def __init__(self):
        super().__init__()

        self.padl_seg_user = []
        self.create_paddle(U_POSITIONS, self.padl_seg_user)

        self.padl_seg_comp = []
        self.create_paddle(C_POSITIONS, self.padl_seg_comp)
        
    def create_paddle(self, positions, pd_segments):
        for starting_position in positions:
            pd_seg = Turtle("square")
            pd_seg.color("white")
            pd_seg.penup()
            pd_seg.goto(starting_position)
            pd_segments.append(pd_seg)

    def move_paddle(self, segm_list, direction):
        for segment in range(len(segm_list)):
            segm_list[segment].setheading(direction)
            segm_list[segment].forward(20)
        
    def move_up(self):
        # Head upwards
        if self.padl_seg_user[-1].ycor() < 280:
            self.move_paddle(self.padl_seg_user, UP)

    def move_down(self):
        # Head downwards
        if self.padl_seg_user[0].ycor() > -280:
            self.move_paddle(self.padl_seg_user, DOWN)

    def move_paddle_comp(self):
        for seg in range(len(self.padl_seg_comp) - 1, 0, -1):
            coordinates = self.padl_seg_comp[seg - 1].position()
            self.padl_seg_comp[seg].goto(coordinates)
        
    def comp_paddle(self):
        if self.padl_seg_comp[0].ycor() > -280:
            self.padl_seg_comp[0].setheading(DOWN)
            self.move_paddle_comp()
            self.padl_seg_comp[0].forward(20)
        else:
            self.padl_seg_comp.reverse()
            if self.padl_seg_comp[0].ycor() < 280:
                self.padl_seg_comp[0].setheading(UP)
                self.move_paddle_comp()
                self.padl_seg_comp[0].forward(20)



