import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

input_user = int(input("What did you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
user = game[input_user]
print(user)

print("Computer choice")
computer = random.choice(game)
print(computer)

if user == computer:
  print("Draw!")
elif (user == rock and computer == scissors) or (user == paper and computer == rock) or (user == scissors and computer == paper):
  print("You win!")
else:
  print("You lost!")


