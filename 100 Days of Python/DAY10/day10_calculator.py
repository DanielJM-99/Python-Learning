# Calculator
from art import calculator_logo

print(calculator_logo)

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

# Ask user to type the first number
first_num = float(input("Type first number: "))

continue_operation = True
while continue_operation:

    # Ask for math operator
    operator = input("+ \n- \n* \n/ \nWhat operation do you want: ")

    # Ask user for second number
    second_num = float(input("Type second number: "))

    answer = operations[operator](first_num, second_num)
    print(f"The solition to: {first_num} {operator} {second_num} is {answer}")

    keep_calculating = input(f"Do you want to keep calculating {answer}, Type 'y' to continue or 'n' to start a new calculation: ").lower()

    if keep_calculating == "y":
        first_num = answer
    else:
        # Ask user to type the first number
        print("\n" * 20)
        print(calculator_logo)
        first_num = float(input("Type first number: "))
