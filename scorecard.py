from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.score_level()
        self.hideturtle()
        self.color("black")

    def game_over(self):
        game = Turtle()
        game.write("Game Over", align="center", font=FONT)

    def write_score(self):
        self.write(f"Level: {self.level}", font=FONT)

    def score_level(self):
        self.goto(-290, 250)
        self.write_score()

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write_score()
