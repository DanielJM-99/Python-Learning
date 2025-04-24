import turtle
import pandas

screen = turtle.Screen()
screen.title("US. States Game ")
image = "./100 Days of Python/DAY25/us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./100 Days of Python/DAY25/us_states_game/50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # states_to_learn_csv
        missing_states = []
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Get specific row of table/dataframe
        state_data = data[data.state == answer_state]
        # Get specific value of a spec column .column.item()
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
