import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_MOVE_DISTANCE

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=1, stretch_wid=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(270)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def next_level(self):
        self.car_speed+=10
