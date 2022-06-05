import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.single_car()
    car_manager.random_move()

    if player.ycor() > 250:
        scoreboard.next_level()
        player.player_reset()
        car_manager.speed_change()

    for i in range(0, len(car_manager.allcars)):
        if car_manager.allcars[i].distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
