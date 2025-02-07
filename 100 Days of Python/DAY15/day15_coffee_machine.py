# CODE FOR A COFFEE MACHINE
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    # Added money
    "money" : 0
}

# TODO 4: CHECKS FOR SUFFICIENT RESOURCES
def check_resources(coffe_menu, coffee_resources, c_choice):
    """Takes MENU, machine resources and customer choice to check if there are 
    enough resources to make coffee, returns True or False"""
    count = 0
    if c_choice == "espresso" or c_choice == "latte" or c_choice == "cappuccino":
        coffe_ingred = coffe_menu[c_choice]["ingredients"]
        for c_resource in coffe_ingred:
            if coffee_resources[c_resource] > coffe_ingred[c_resource]:
                count += 1
            else:
                count = 0
                print(f"Sorry there is not enough {c_resource}")
        if (count == 2 and c_choice == "espresso") or count == 3 :
            print(f"We can prepare {c_choice}")
            return True
        else:
            print(f"Coffe machine can't prepare {c_choice}")
            return False

# TODO 5: PROCESS COINS
def process_coins():
    """Aks user for coins and gives back the sum of all as total"""
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    total = round(quarters + dimes + nickles + pennies, 2)
    # print(f"The total amount put in is: ${total}")
    return total

# TODO 6: CHECK TRANSACTION 
def check_transaction(coffe_menu, c_choice):
    """Checks if users had enough money to purchase drink and returns True or False"""
    user_money = process_coins()
    coffee_price = coffe_menu[c_choice]["cost"]
    if user_money >= coffee_price:
        resources["money"] += coffee_price
        if user_money > coffee_price:
            change = round(user_money - coffee_price, 2)
            print(f"Here is ${change} dollars in change. ")
            return True
    else:
        print("Sorry not enough money to prepare drink. Money refunded. ")
        return False

def make_coffee(coffee_menu, machine_resources):
    """Takes the menu and resources, makes the coffee and 
    substract ingredients from the machine"""
    coffee_ingredients = coffee_menu[choice]["ingredients"]
    for ingredients in coffee_ingredients:
        machine_resources[ingredients] -= coffee_ingredients[ingredients]
    print(f"Here is your {choice}. Enjoy!. ")

turned_on = True 

while turned_on:
    
    # TODO 1: PROMPT USERS
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 3: REPORT RESOURCES
    if choice == "report":
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: {resources["money"]}")

    enough_resources = check_resources(coffe_menu=MENU, coffee_resources=resources, c_choice=choice)

    # TODO 7: MAKE COFFEE
    if enough_resources:
        enough_money = check_transaction(coffe_menu=MENU, c_choice=choice)
        if enough_money:
            make_coffee(coffee_menu=MENU, machine_resources=resources)

    # TODO 2: TURN OFF MACHINE
    elif choice == "off":
        turned_on = False
        