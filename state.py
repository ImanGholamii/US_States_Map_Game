from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def move(self, position: tuple):
        self.goto(position)

    def show_state_name(self, state_name: str):
        self.write(f"{state_name}")
