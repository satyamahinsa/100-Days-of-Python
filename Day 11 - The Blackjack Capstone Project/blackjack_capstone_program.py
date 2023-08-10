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

import os
import random
from blackjack_capstone_art import logo

def pickCard():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculateScore(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compareScore(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose!"
  
  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "Lose, opponent has a Blackjack!"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21: 
    return "Opponent went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  for _ in range(0, 2):
    user_cards.append(pickCard())
    computer_cards.append(pickCard())

  continue_play = True
  while continue_play:
    user_score = calculateScore(user_cards)
    computer_score = calculateScore(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score >= 21:
      continue_play = False
    else:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == 'y':
        user_cards.append(pickCard())
      else:
        continue_play = False
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(pickCard())
    computer_score = calculateScore(computer_cards)
    
  print(f"Your final cards: {user_cards}, current score: {user_score}")
  print(f"Computer's final card: {computer_cards}, current score: {computer_score}")
  print(compareScore(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  os.system("cls")
  play_game()
