from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(-275, 250)
        self.level = 1
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.color("chocolate")
        self.write("Game Over!", align="center", font=("Courier", 32, "bold"))
