from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def end_of_game(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=FONT)
