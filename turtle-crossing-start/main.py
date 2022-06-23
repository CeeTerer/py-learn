import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("white")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.4)
    screen.update()
    screen.onkey(player.move_up, "Up")

    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect when crosses
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()