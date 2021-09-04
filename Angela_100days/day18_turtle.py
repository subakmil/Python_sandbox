from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")


pace = 90


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R, G, B)


for _ in range(3, 9):
    pace += 10
    angle = 360 / _
    change_color()

    for i in range(_):
        tim.forward(pace)
        tim.right(angle)


screen = Screen()
screen.exitonclick()
