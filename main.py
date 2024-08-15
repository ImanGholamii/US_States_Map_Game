import turtle
import pandas as pd
from state import State
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # path of image
turtle.shape(image)

state = State()
scoreboard = Scoreboard()
current_score = 0


def make_question():
    """Ask user state guess"""
    user_input = screen.textinput(title=f"{current_score}/50 States name", prompt="What's another state name?")
    return user_input.title()


data = pd.read_csv("50_states.csv")


def check_answer(user_input):
    """check user input exist or not"""
    if data.state.str.contains(user_input).any():
        print(data[data.state == user_input])
        return True


def take_position(user_input):
    """Extract x, y coordinate from data file"""
    filtered_data = data[data.state == user_input]
    x_coord = int(filtered_data.x.iloc[0])
    y_coord = int(filtered_data.y.iloc[0])
    coord = (x_coord, y_coord)
    return coord


mentioned_countries = []
game_is_on = True
while game_is_on:
    state_name = make_question()
    if check_answer(user_input=state_name):
        mentioned_countries.append(state_name)
        current_score = len(mentioned_countries)
        print(mentioned_countries)
        coordinates = take_position(user_input=state_name)
        state.move(coordinates)
        state.show_state_name(state_name=state_name)

screen.exitonclick()
