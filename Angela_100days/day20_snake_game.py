from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# TODO1: Create a snake body

tim = Turtle(shape="square")
tim.color("white")
tim.penup()


screen.exitonclick()
