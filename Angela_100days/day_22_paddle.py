from turtle import Turtle

COLOR = "white"
WIDTH = 5
LEN = 1

class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LEN)
        self.penup()
        self.goto(x=x_pos, y=y_pos)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
        
        