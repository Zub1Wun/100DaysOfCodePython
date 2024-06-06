#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# MAKE COMMENTS or those FUNCTION Descrtions etc.
# Check Asci prints out well, perhaps make it print out line by line?
# Make better variable names

import random
import art

EASY_LEVEL_ATTEMPTS= 10
HARD_LEVEL_ATTEMPTS = 5

def difficulty_choice():
    while True:
        difficulty = input("Choose a difficulty level: easy or hard\n")
        if difficulty == "easy" or difficulty == "Easy" or difficulty == "EASY":
            return EASY_LEVEL_ATTEMPTS
        elif difficulty == "hard" or difficulty == "Hard" or difficulty == "HARD":
            return HARD_LEVEL_ATTEMPTS
        else:
            print("Incorrect input! Try again")
            continue

def generate_random_number():
    return random.randint(1,100)

def check_answer(guess, answer, turns):
    if guess < answer:
        print("\nToo low.\nGuess again.")
        return turns - 1
    elif guess > answer:
        print("\nToo high.\nGuess again.")
        return turns - 1
    elif guess == answer:
        print("\nCorrect!")
        return

def run_game(param_guesses, param_random_number):
    guesses = param_guesses
    random_number = param_random_number

    guess = 0
    while guess != random_number:
        print("Guess a number between 1 and 100")
        print(f"You have {guesses} attempts remaining to guess the number")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("Incorrect input, enter an integer value")
            guess = int(input("Make a guess: "))
        guesses = check_answer(guess, random_number, guesses)
        if guesses == 0:
            print("You've run out of guesses, you lose!")
            print(f"The correct answer was {random_number}")
            return

def main():
    print(art.logo)
    while True:
        response = input("Do you want to play a game? Type 'y' or 'n': ")
        if response == 'n':
            print("Goodbye!")
            quit()
        elif response == 'y':
            run_game(difficulty_choice(), generate_random_number())   
        else:
            choice = input("\nIncorrect input\n Please press any key and try again\n")
        continue 

main()
