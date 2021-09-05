from turtle import Turtle, Screen, colormode
import random
import colorgram

colormode(255)
tim = Turtle()
# tim.shape("turtle")


# def change_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()

#     tim.color(R, G, B)

# region Previous Projects
# for _ in range(3, 9):
#     pace += 10
#     angle = 360 / _
#     change_color()

#     for i in range(_):
#         tim.forward(pace)
#         tim.right(angle)

# # Random Walk Challenge
# tim.pensize(5)
# tim.speed(0)

# choices = ["front", "right", "left", "back"]
# colors = ["black", "dark cyan", "olive", "dark red"]
# progress = 0


# while progress < 201:
#     progress += 1
#     to = random.choice(choices)
#     change_color()
#     if to == "front":
#         tim.forward(15)
#     elif to == "right":
#         tim.right(90)
#         tim.forward(15)
#     elif to == "left":
#         tim.left(90)
#         tim.forward(15)
#     else:
#         tim.left(180)
#         tim.forward(15)

# # Spirograph challenge

# angle = 0
# tim.speed(0)

# while angle < 360:
#     change_color()
#     tim.circle(150)

#     angle += 5
#     tim.setheading(angle)
# endregion

# region Hirst Painting
# colors = colorgram.extract(
#     "C:/Users/Milos Subak/OneDrive/VS Code projects/_Python_sandbox/Angela_100days/hirst_painting.jpg", 20)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(1, 9, 29), (121, 96, 42), (238, 211, 72), (77, 34, 23), (221, 80, 59), (225, 117, 100), (92, 1, 21), (178, 140, 171),
              (151, 92, 116), (35, 90, 26), (8, 154, 73), (204, 64, 92), (220, 178, 219), (167, 129, 76), (1, 63, 146), (4, 220, 218)]

tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100

for i in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# endregion

screen = Screen()
screen.exitonclick()
