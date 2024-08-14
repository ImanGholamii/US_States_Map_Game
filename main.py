import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # path of image
turtle.shape(image)


def make_question():
    """Ask user state guess"""
    user_input = screen.textinput(title="Guess states name", prompt="What's another state name?")
    return user_input.title()


data = pd.read_csv("50_states.csv")


def check_answer(user_input):
    """check user input exist or not"""
    if data.state.str.contains(user_input).any():
        print(data[data.state == user_input])


game_is_on = True
while game_is_on:
    state_name = make_question()
    check_answer(user_input=state_name)

screen.exitonclick()
