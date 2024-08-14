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
        return True


def take_position(user_input):
    """Extract x, y coordinate from data file"""
    filtered_data = data[data.state == user_input]
    x_coord = int(filtered_data.x)
    y_coord = int(filtered_data.y)
    coordinates = (x_coord, y_coord)
    return coordinates


game_is_on = False
while game_is_on:
    state_name = make_question()
    check_answer(user_input=state_name)

screen.exitonclick()
