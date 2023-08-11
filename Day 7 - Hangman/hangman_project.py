import random
from hangman_art import logo, stages

animal_words = ["bull", "paradise", "sheep", "tiger", "kangaroo"]

selected_word = random.choice(animal_words)
remaining_life = 6

user_guess_result = []
for n in range(len(selected_word)):
  user_guess_result.append("_")
  
print(logo)
print("Theme Word is Animal")

while "_" in user_guess_result:
  guess_user = input("Guess a letter: ").lower()
  
  if guess_user in user_guess_result:
    print(f"You guessed {guess_user}")

  for position in range(len(selected_word)):
    letter = selected_word[position]
    if guess_user == letter:
      user_guess_result[position] = letter

  if guess_user not in selected_word:
    print(f"You guessed {guess_user}, it is not in word. You lose 1 life.")
    remaining_life -= 1
    if remaining_life == 0:
      print("You lost")
      break
  
  print(f"{' '.join(user_guess_result)}")
  print(stages[remaining_life])
else:
  print("You won!")

print(stages[remaining_life])