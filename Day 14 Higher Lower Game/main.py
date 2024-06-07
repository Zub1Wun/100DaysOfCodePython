from random import randint #import random, then use random.choice or import choice from random
import art  # from art import logo, vs
import game_data # from game_data import data

"""
HAVE A CHECK if description starts with a vowel, if it does, then write 'an' not 'a'

ALSO KEEP CORRECT ITEM and change second one only, not both

CLEAR SCREEN AFTER EACH ROUND
"""

def correct_selection(selection, item_A, item_B):
    if selection == 'A' and item_A['follower_count'] > item_B['follower_count']:
        return True
    elif selection == 'B' and item_A['follower_count'] < item_B['follower_count']:
        return True


def get_random_item():
    # random.choice(data)
    return game_data.data[randint(0,(len(game_data.data))-1)]

def run_game():
    # Keep track of score
    # While loop to continue game until incorrect guess
    answer_correct = True
    score = 0
    while answer_correct==True:
        

        print(art.logo)
        item_A = get_random_item()
        item_B = get_random_item()

        while item_A == item_B:
            if item_B == item_A:
                item_B = get_random_item()
        
        ### FORMAT item data into printable
        """
        item_name = item_A['name']
        item_desc = item_A['description']
        item_country = item_A['country']
        #### instead of this, make into a function, 
        that returns f-string independent of whether item A or B

        """
        
        print(f"Compare A: {item_A['name']}, a {item_A['description']}, from {item_A['country']}")
        print(art.vs)
        print(f"Against B: {item_B['name']}, a {item_B['description']}, from {item_B['country']}")

        #if correct_selection(user_selection, item_A, item_B):
        while True:
            user_selection = input("Who has more followers? Type 'A' or 'B': ").upper()
            if user_selection == 'A' or user_selection == 'B':
                if correct_selection(user_selection, item_A, item_B):
                    score += 1
                    print(f"You're right! Current score: {score}")
                    break
                else:
                    print(f"Sorry, that's wrong. Final score: {score}")
                    answer_correct = False
                    break
            else:
                print("Incorrect input! Type 'A' or 'B'")
                continue

    print(user_selection)
    


    # Check is user inputs correctly
    # Check if user was wrong or right
    # If right, increment score and run again.
    # If wrong, print out score and ask to play again

def main():
    run_game()

main()