# Simple calculator, cant digit non number or non operators.
print("Welcome to the simple calculator")
print("--------------------------------")

#Ask for users input until user puts numbers
while True:
    try:
        first_num = float(input("What's the first number?: "))
        second_num = float(input("What's the second number?: "))    
    except ValueError:
        print("Invalid number")
    else:
        break

# Operations list
operations = ["+", "-", "*", "/"]  

# Ask for operation until it meets one in the list and makes operation
not_ready = True
while not_ready:
    # Ask user for operation
    operation_choice = input("What operation do you want to make? Sum(+), Subs(-), Mult(*), Div(/))> ") 
    # Valids correct operation
    if operation_choice in operations:
        if operation_choice == "+":
            print(f"Result = {first_num + second_num}")
        elif operation_choice == "-":
            print(f"Result = {first_num - second_num}")
        elif operation_choice == "*":
            print(f"Result = {first_num * second_num}")
        elif operation_choice == "/":
            if second_num != 0:
                print(f"Result = {first_num / second_num}")
            else:
                print("Can't divide by 0")
        not_ready = False
    else:
        print("Wrong operator")
