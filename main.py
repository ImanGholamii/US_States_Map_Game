import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # path of image
turtle.shape(image)

def make_question():
    """Ask user state guess"""
    user_input = screen.textinput(title="Guess states name", prompt="What's another state name?")
    return user_input.title()


game_is_on = True
while game_is_on:
    state_name = make_question()
    pass

screen.exitonclick()
