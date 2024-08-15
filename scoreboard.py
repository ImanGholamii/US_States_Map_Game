from turtle import Turtle

FONT = ('arial', 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """update and show score"""
        self.clear()
        self.write(f"{self.score}/50", font=FONT)

    def add_score(self):
        """add point"""
        self.score += 1
