from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")


# pace = 90


# def change_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()

#     tim.color(R, G, B)


# for _ in range(3, 9):
#     pace += 10
#     angle = 360 / _
#     change_color()

#     for i in range(_):
#         tim.forward(pace)
#         tim.right(angle)

# Random Walk Challenge
tim.pensize(3)
tim.speed(0)

choices = ["front", "right", "left", "back"]
colors = ["black", "dark cyan", "olive", "dark red"]
progress = 0


while progress < 1001:
    progress += 1
    to = random.choice(choices)
    tim.color(random.choice(colors))
    if to == "front":
        tim.forward(10)
    elif to == "right":
        tim.right(90)
        tim.forward(10)
    elif to == "left":
        tim.left(90)
        tim.forward(10)
    else:
        tim.left(180)
        tim.forward(10)


screen = Screen()
screen.exitonclick()
