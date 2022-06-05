from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.level_update()

    def level_update(self):
        self.goto(-120, 250)
        self.write(f"level : {self.level}", align="right", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.level_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
