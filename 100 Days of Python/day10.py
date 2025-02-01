# Calculator
from art import calculator_logo

# Todo Write out other 3 functions - subtract, multiply, divide

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Todo add 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+" : add,  # Change name of functions
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():

    print(calculator_logo)

    # Ask user to type the first number
    first_num = float(input("Type first number: "))

    continue_operation = True
    while continue_operation:

        operator = input("\n+ \n- \n* \n/ \nWhat operation do you want: ")
        second_num = float(input("Type second number: "))
        answer = operations[operator](first_num, second_num)
        
        print(f"The solition to: {first_num} {operator} {second_num} is {answer}")

        keep_calculating = input(f"Do you want to keep calculating with {answer}, Type 'y' to continue or 'n' to start a new calculation: ").lower()
        if keep_calculating == "y":
            first_num = answer
        else:
            continue_operation = False
            print("\n"*20)
            calculator()

calculator()
    