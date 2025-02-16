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
}

#TODO: 3. Create function for reporting the resources and money in the coffee machine
def report(prompt):
    if prompt.lower() == "report":
        report_card = f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}ml"""
        return report_card


#TODO: 2. Add user input functions with basic error handling
def user_input_number():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def user_input_string():
    while True:
        try:
            return input("What would you like? (espresso/latte/cappuccino): ")
        except ValueError:
            print("Invalid input. Please enter a expresso/latte/cappuccino")


user_choice = user_input_string()
#TODO: 4. Turn off Coffee Machine
while user_choice.lower() != "off":
    #TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    user_choice = user_input_string()

    print(report(user_choice))