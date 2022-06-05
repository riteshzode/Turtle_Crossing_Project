import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.STARTING_MOVE_DISTANCE = 5
        self.allcars = []

    def single_car(self):
        if random.randint(0, 6) == 1
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            y = random.randint(-240, 240)
            new_car.goto(300, y)
            self.allcars.append(new_car)

    def random_move(self):
        for i in self.allcars:
            i.forward(self.STARTING_MOVE_DISTANCE)

    def speed_change(self):
        self.STARTING_MOVE_DISTANCE += 5
