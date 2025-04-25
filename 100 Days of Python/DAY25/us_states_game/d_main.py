import turtle
import pandas

screen = turtle.Screen()
screen.title("US. States Game ")
image = "./100 Days of Python/DAY25/us_states_game/blank_states_img.gif"
# Add shape give you the ability to put a .gif image as a screen
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)

# Open and read csv with states and locatation
states_data = pandas.read_csv("./100 Days of Python/DAY25/us_states_game/50_states.csv")
score = 0
all_states = states_data.state.to_list()

game_on = True
while game_on:

    screen.update()
    answer_state = screen.textinput(title=f"({score}/50) States Correct", prompt="What's another state's name?")

    # Get specific info if answer matches csv file
    ## Get x,y coord
    state_row = states_data[states_data.state == answer_state]
    x_value = state_row.x.to_list()[0]
    y_value = state_row.y.to_list()[0]

    ## Write states name into map and move to correct location
    answer_text = turtle.Turtle()
    answer_text.hideturtle()
    answer_text.penup()
    answer_text.goto(x_value, y_value)
    answer_text.write(f"{answer_state}", align="center", font=('Arial', 8, 'normal'))
    
    ## If correct update score, ask again and repeat
    if answer_state in all_states:   
            score += 1

screen.exitonclick()