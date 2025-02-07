# import another_module
# print(another_module.another_var)

from turtle import Turtle, Screen

# Created a turtle object from the Turtle class. () to construct the object
timmy = Turtle()
my_screen = Screen()
my_screen.canvheight
print(my_screen.canvheight)
my_screen.exitonclick()

""" 
from turtle import Turtle, Screen

# Created a turtle object from the Turtle class. () to construct the object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# Draw a square 4 times
for length in range(1, 5):
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)

my_screen = Screen()
my_screen.canvheight
print(my_screen.canvheight)
my_screen.exitonclick()
"""

from prettytable import PrettyTable

# Creates object
table = PrettyTable()
# Use method to add columns
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)