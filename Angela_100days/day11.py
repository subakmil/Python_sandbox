import os
import sys
sys.path.append("C:/Users/Milos Subak/OneDrive/VS Code projects/_Python_sandbox/Art")
from blackjack import logo
import random

if input("Do you want to play some Blackjack, bro?? ('y'/'n')\n") == "n":
    sys.exit()

os.system("cls")
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack_game():
    user_numbers = [random.choice(cards), random.choice(cards)]
    user_score = sum(user_numbers)

    dealer_numbers = [random.choice(cards)]

    print(f"Your cards: {user_numbers}, current score: {user_score}\nDealer's first card: {dealer_numbers}")
    while sum(dealer_numbers) < 14:
        dealer_numbers.append(random.choice(cards))
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card != "y" and another_card != "n":
            print("Bro, you entered wrong input, try it again.")
        elif another_card == "n":
            if (21 - sum(user_numbers)) < abs(21 - sum(dealer_numbers)):
                result = "Horaay! You Win!"
            elif (21 - sum(user_numbers)) == abs(21 - sum(dealer_numbers)):
                result = "It's a draw. Try it Again!"
            else:
                result = "Sorry, bro. Now you lose."
            return f"Your final hand: {user_numbers}. Your score is {sum(user_numbers)}\nDealer's final hand: {dealer_numbers}. Dealer's score is {sum(dealer_numbers)}\n{result}"
        else:
            user_numbers.append(random.choice(cards))
            if sum(user_numbers) > 21:
                return f"Your cards: {user_numbers}. Your score: {sum(user_numbers)}. Sorry, you lose."
            else:
                print(f"Your cards: {user_numbers}, current score: {sum(user_numbers)}")


print(blackjack_game())
continue_playing = True
while continue_playing:
    if input("Do you want play another game? ('y'/'n')\n") == "y":
        os.system("cls")
        print(logo)
        print(blackjack_game())
    else:
        continue_playing = False
