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

# General setup
continue_code = True
list_of_options = ["espresso", "latte", "cappuccino", "off", "report"]

# TODO1: User requirements (espresso/latte/cappuccino)
#choice = input("What would you like? (espresso/latte/cappuccino): ")

# TODO2: Turn off the coffe machine by entering "off" to the prompt


def selection():
    bad_answer = True
    while bad_answer:
        loop_choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if loop_choice not in list_of_options:
            print(
                f"Please, select one of the given options. Unfortunately we do not serve {loop_choice}.")
        else:
            bad_answer = False
            return loop_choice


choice = selection()
if choice != "off":
    print({choice})
