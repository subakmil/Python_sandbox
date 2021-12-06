import time
from turtle import Screen
from day23_player import Player
from day23_car_manager import CarManager
from day23_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tony = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(tony.go, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect car collision
    for car in car_manager.all_cars:
        if car.distance(tony) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    # Detect successful crossing
    if tony.is_at_finish_line():
        tony.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        

screen.exitonclick()
