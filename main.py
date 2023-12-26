import turtle
import pandas as pd


def get_state_data(answer, states_data):
    """Retrieve state data for a given state name."""
    return states_data[states_data.state.str.lower() == answer.lower()]


def write_state_name(turtle, state_data):
    """Write the state's name on the map."""
    turtle.goto(int(state_data.x), int(state_data.y))
    turtle.write(state_data.state.item(), align="center")


def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    states_data = pd.read_csv("50_states.csv")
    states = states_data.state.str.lower().to_list()
    guessed_states = []

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    try:
        while len(guessed_states) < 50:
            answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed",
                                            prompt="What's another state name?")

            if answer_state is None:
                break  # Handle NoneType if user cancels the input dialog

            answer_state = answer_state.title()

            if answer_state.lower() == "exit":
                break

            if answer_state.lower() in states and answer_state.lower() not in guessed_states:
                guessed_states.append(answer_state.lower())
                state_data = get_state_data(answer_state, states_data)
                write_state_name(writer, state_data)
    except turtle.Terminator:
        print("Game closed.")
    finally:
        missing_states = states_data[~states_data.state.str.lower().isin(guessed_states)]
        missing_states.to_csv("missing_states.csv")
        turtle.bye()


if __name__ == "__main__":
    main()

