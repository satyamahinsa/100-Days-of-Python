from random import randint 

EASY_LEVEL_ATTEMPTS = 10 
HARD_LEVEL_ATTEMPTS = 5 

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_ATTEMPTS
  elif level == "hard":
    return HARD_LEVEL_ATTEMPTS


def check_answer(guess, answer, attempts):
  if guess > answer:
    print("Too High.")
    return attempts - 1
  elif guess < answer:
    print("Too Low.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {answer}.")


def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  random_number = randint(1, 100)
  
  attempts = set_difficulty()
  print(f"You have {attempts} attempts remaining to guess the number.")
  
  guess = 0
  while guess != random_number:
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, random_number, attempts)
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != random_number:
      print("Guess again!")

game()