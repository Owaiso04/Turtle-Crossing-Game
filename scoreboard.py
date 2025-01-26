from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.level = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(font=FONT, arg=f"Level: {self.level}")

    def lose(self):
        self.goto(0, 0)
        self.write(font=FONT, arg="Game Over.")
