import random

import art

art.logo_guessing_game

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

def difficulty_level():
    while True:
        level = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if level == "easy":
            return 10
        elif level == "medium":
            return 5
        elif level == "hard":
            return 3
        else:
            print("Invalid choice. Please choose 'easy', 'medium', or 'hard'.")
def guess_number(target, attempts):
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {target} in {attempt} attempts!")
            return
    print(f"Sorry, you've used all {attempts} attempts. The correct number was {target}.")



target_number = random.randint(1, 100)  # You can change this to any number you want
max_attempts = difficulty_level()  # You can change this to set the number of attempts
guess_number(target_number, max_attempts)

print("Thanks for playing the Number Guessing Game!")
