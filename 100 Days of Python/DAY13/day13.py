# Debugger

import random 
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    # Change indentetaion so it works, find out with a debugger
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 4, 5, 7, 8])