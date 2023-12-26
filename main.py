import turtle
import pandas as pd

def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    states_data = pd.read_csv("50_states.csv")
    states = states_data.state.to_list()
    guessed_states = []

    while len(guessed_states) < len(states):
        answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} guessed", prompt="What's another state name?").title()
        if answer_state in states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = states_data[states_data.state == answer_state]
            t.goto(int(state_data.x.item()), int(state_data.y.item()))
            t.write(state_data.state.item())

    turtle.mainloop()

if __name__ == "__main__":
    main()