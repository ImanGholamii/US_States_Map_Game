from turtle import Turtle

FONT = ("Comic Sans MS", 10, "")
ALIGNMENT = 'center'


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move(self, position):
        self.goto(position)

    def show_state_name(self, state_name: str):
        self.write(f"{state_name}", align=ALIGNMENT, font=FONT)
