import os
import sys
sys.path.append(
    "C:/Users/Zasilkovna/OneDrive - Packeta/Osobní/VS Code/_Python_sandbox/Art")
from blackjack import logo
import random

if input("Do you want to play some Blackjack, bro?? ('y'/'n')\n") == "n":
    sys.exit()

os.system("cls")
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack_game():
    user_num1 = random.choice(cards)
    user_num2 = random.choice(cards)
    user_score = user_num1 + user_num2

    dealer_num1 = random.choice(cards)

    print(f"Your cards: [{user_num1}, {user_num2}], current score: {user_score}\nDealer's first card: {dealer_num1}")

blackjack_game()
