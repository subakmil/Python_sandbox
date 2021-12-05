from turtle import Screen
from day_22_paddle import Paddle
from day_22_ball import Ball
from day_22_scoreboard import Scoreboard
import time

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
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_player.go_up, "Up")
screen.onkey(right_player.go_down, "Down")
screen.onkey(left_player.go_up, "w")
screen.onkey(left_player.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with r_player paddle
    if ball.distance(right_player) < 50 and ball.xcor() > 320 or ball.distance(left_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect rigth miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# ednregion - Main Code

screen.exitonclick()

