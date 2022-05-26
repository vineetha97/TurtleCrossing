from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scorecard import Scorecard
screen = Screen()

screen.setup(height=600, width=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scorecard = Scorecard()
game_is_on = True

screen.listen()
screen.onkey(player.up, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_cars()
    car_manager.move()

    for car in car_manager.all_cars:

        if car.distance(player) < 20:
            scorecard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.reset_position()
        scorecard.increase_score()
        car_manager.next_level()

screen.exitonclick()
