from turtle import Screen, right
from day_22_paddle import Paddle

# region - Setup Environment

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # Turning off screen animation
screen.listen()

# endregion _Setup Environment

# region - Main Code

right_player = Paddle(350, 0)
left_player = Paddle(-350, 0)

screen.onkey(right_player.go_up, "Up")
screen.onkey(right_player.go_down, "Down")
screen.onkey(left_player.go_up, "w")
screen.onkey(left_player.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()












# ednregion - Main Code

screen.exitonclick()

