## stop-ai-prompts

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

## stop-ai-prompts

import art
import random

CONST_CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  print("~~~CARD DEALT~~~")
  #cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(CONST_CARDS)

def valid_response(response):
  valid_response = False
  while not valid_response:
    if response == 'n' or response == 'y':
      return response
    else:
      print("Invalid response!\n")
      response = input("Input correct response: ")

def print_hands_final(player_cards, computer_cards):
  print("~~~FINAL HANDS~~~")
  player_score = sum(player_cards)
  computer_score = sum(computer_cards)
  print(f"Your hand: {player_cards} and your score: {player_score}")
  print(f"Computer hand: {computer_cards} and your score: {computer_score}")

def print_hands(player_cards, computer_cards):
  print("~~~YOUR HAND~~~")
  player_score = sum(player_cards)
  print(f"Your hand: {player_cards} and your score: {player_score}")
  print(f"Computer's first card: {computer_cards[0]}")

def another_card(player_cards, computer_cards):
  print("~~~ANOTHER CARD~~~")

  computer_score = sum(computer_cards)
  if computer_score < 16:
    computer_cards.append(deal_card())
    computer_score = sum(computer_cards)

  player_cards.append(deal_card())
  player_score = sum(player_cards)
  if player_score > 21 and computer_score <= 21:
    print_hands_final(player_cards, computer_cards)
    print("You lose!")
    return main()
  elif computer_score > 21 and player_score <= 21:
    print_hands_final(player_cards, computer_cards)
    print("You win!")
    return main()
  elif computer_score < 21 and player_score < 21:
    print_hands(player_cards, computer_cards)
    return play_game(player_cards, computer_cards)
  
def pass_hand(player_cards, computer_cards):
  print("~~~PASS HAND~~~")
  player_score = sum(player_cards)
    
  computer_score = sum(computer_cards)
  """
  if computer_score > 16:
    computer_cards.append(deal_card())
    computer_score = sum(computer_cards)
  """

  print_hands_final(player_cards, computer_cards)
  if player_score > 21 and computer_score <= 21:
    print("You lose!")
  elif computer_score > 21 and player_score <= 21:
    print("You win!")
  elif player_score > computer_score:
    print("You win!")
  elif player_score < computer_score:
    print("You lose!")
  else:
    print("DRAW!")

  return main()

def start_game(player_cards, computer_cards):
  print("~~~START GAME~~~")
  print(art.logo)
  player_cards.extend([deal_card(), deal_card()])
  computer_cards.extend([deal_card(), deal_card()])
  print_hands(player_cards, computer_cards)
  play_game(player_cards, computer_cards)

def play_game(player_cards, computer_cards):
  print("~~~PLAY GAME~~~")
  while True:
    response = input ("Type 'y' to get another card, type 'n' to pass: ")
    if response == 'n':
      print("Pass!")
      pass_hand(player_cards, computer_cards)
    elif response == 'y':
      print("Yes")
      another_card(player_cards, computer_cards)
    else:
      choice = input("\nIncorrect input\n Please press any key and try again\n") 

def main():
  print("~~~MAIN~~~")
  player_cards = []
  computer_cards = []
  while True:
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if response == 'n':
      print("Goodbye!")
      quit()
    elif response == 'y':
      start_game(player_cards, computer_cards)      
    else:
      choice = input("\nIncorrect input\n Please press any key and try again\n")
      continue 

main()


  




print("END OF PROGRAM")
    