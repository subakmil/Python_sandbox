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
play_game = True
list_of_options = ["espresso", "latte", "cappuccino", "off", "report"]
money_in = 0
our_money = 0

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


def coin_calculator():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies


while play_game:
    choice = selection()
    if choice == "off":
        play_game = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${our_money}")
    else:
        cost = MENU[choice]["cost"]
        if resources["water"] < MENU[choice]["ingredients"]["water"] or resources["milk"] < MENU[choice]["ingredients"]["milk"] or resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
            print("Sorry, there is not enough resources to proceess your order. Our service team will fix this issue soon. Thank you for you understanding.")
            play_game = False
        else:
            print(f"{choice} costs ${cost}\nPlease insert the money.")
            money_in += coin_calculator()
            if money_in == cost:
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                print("Thank you. Here is your drink.")
                our_money += MENU[choice]["cost"]
            elif money_in < cost:
                print(
                    f"Not enough money. You inserted ${money_in} and the cost of the drink is ${cost}. Here is your money back and try again.")
                money_in = 0
            else:
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                print(
                    f"Here is your drink and ${round(money_in - cost, 2)} back. Enjoy your drink.")
                money_in = 0
                our_money += MENU[choice]["cost"]
