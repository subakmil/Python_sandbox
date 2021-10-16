from turtle import Turtle

START = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in START:
            new_piece = Turtle(shape="square")
            new_piece.color("white")
            new_piece.penup()
            new_piece.setposition(position)
            self.segments.append(new_piece)

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
    
        self.segments[0].forward(MOVE_DISTANCE)
