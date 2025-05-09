# import pandas 

# 1: Get the coordinates of states map of mexico
# 2: Put values in table 
# 3: Put image and create dataframe
# 4: With turtle module create screen, input for user and write to screen
# 5: Create list of states 
# 6: Match the user input with states
## If correct write it in the coordinate of the state 

## If not rest lifes of user (0/3)
## WRITE WINNER OR LOSER IF USER gets all the states or if loses all lifes
# 7: After he gets all or user has no lifes end game if user is correct thats it show winning letters if not create csv with all the missing 
# answers 

import turtle 
import pandas 

screen = turtle.Screen()
screen.setup(width=1000, height=700)

image_path = "./100 Days of Python/DAY25/mx_states_game/mexico_map.gif"
screen.addshape(image_path)
turtle.shape(image_path)
screen.tracer(0)

# Get coordinates 
# while True:

#     def get_mouse_click_coor(x, y):
#         print(x, y)

#     turtle.onscreenclick(get_mouse_click_coor)
#     screen.update()

states_data = pandas.read_csv("./100 Days of Python/DAY25/mx_states_game/mx_states.csv")

# Make a list of states using states_data
states_column = states_data.states
state_list = states_column.to_list()

new_turtle = turtle.Turtle()
user_ans = ""
answer_list = []
lifes = 3

while user_ans != "Exit":

    user_ans = screen.textinput(f"SCORE ({len(answer_list)}/32) - LIFES ({lifes}/3)", "NAMES OF THE STATES IN MEXICO? ").title()

    # Check if user answer is in list of states
    if user_ans in state_list and user_ans not in answer_list:
        # If yes write Name in correct coordinate
        state_row = states_data[states_data.states == user_ans]
        x_cord = state_row.x.item()
        y_cord = state_row.y.item()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x_cord, y_cord)
        new_turtle.write(f"{user_ans}", align="center")
        answer_list.append(user_ans)
    if user_ans not in state_list:
        lifes -= 1
    if lifes == 0:
        new_turtle.goto(-100, -50)
        new_turtle.write("YOU HAVE LOST!!", move=False, align='left', font=('Arial', 20, 'normal'))
        break 
    elif len(state_list) == len(answer_list):
        new_turtle.goto(-100, -50)
        new_turtle.write("YOU HAVE WON!! ;)", move=False, align='left', font=('Arial', 20, 'normal'))
        break
        
screen.exitonclick()