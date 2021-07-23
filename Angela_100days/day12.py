# Guess the number game
import random
import os

os.system("cls")
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
looping = True
while looping:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        looping = False
        attempts = 10
    elif difficulty == "hard":
        looping = False
        attempts = 5
    else:
        print(
            "Please select correct level of difficulty")

playing = True
win = False
guess_number = random.choice(range(1, 101))

while playing:
    print(f"You have {attempts} remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess < guess_number:
        print("Too low.")
    elif user_guess > guess_number:
        print("Too high.")
    else:
        playing = False
        win = True
        print(f"Correct! You got it. It was number {guess_number}!\nYou win!")

    if attempts == 1 and not win:
        playing = False
        print(
            f"Sorry, you ran out of attempts. The correct number was {guess_number}.")
    else:
        attempts -= 1
