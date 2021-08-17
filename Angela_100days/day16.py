# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("chartreuse3")
# timmy.fd(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"

# print(table)
import sys
sys.path.append("C:/Users/Zasilkovna/OneDrive - Packeta/Osobní/VS Code/_Python_sandbox/day16_OOP_Coffe_Machine")

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Documentation for the Coffee Machine Project 2:
# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

my_coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                my_coffeemaker.make_coffee(drink)
