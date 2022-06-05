from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        self.goto(STARTING_POSITION)
