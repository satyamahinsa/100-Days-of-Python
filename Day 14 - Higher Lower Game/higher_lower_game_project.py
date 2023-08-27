from game_data import data
import random
from os import system

print("Welcome to the Higher Lower Game!")
print("Theme: Account")

def get_random_account():
  return random.choice(data)

def check_answer(accountA, accountB, answer):
  if accountA["follower_count"] > accountB["follower_count"]:
    return answer == "a"
  else:
    return answer == "b"

def game():
  score = 0
  should_continue = True
  accountA = get_random_account()
  accountB = get_random_account()
  
  
  while should_continue:
    accountA = accountB
    accountB = get_random_account()
    while accountA == accountB:
      accountB = get_random_account()
      
    print()
    print(f"Compare A: {accountA['name']}, {accountA['description']}, from {accountA['country']}.")
    print("VS")
    print(f"Against B: {accountB['name']}, {accountB['description']}, from {accountB['country']}.")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    system("cls")
    if check_answer(accountA, accountB, user_answer):
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      should_continue = False


game()

