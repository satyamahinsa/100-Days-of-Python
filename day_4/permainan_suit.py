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

input_user = int(input("Apa yang Anda pilih? Ketik 0 untuk Batu, 1 untuk Kertas atau 2 untuk Gunting: "))
user = game[input_user]
print(user)

print("Pilihan komputer")
computer = random.choice(game)
print(computer)

if user == computer:
  print("Imbang!")
elif (user == rock and computer == scissors) or (user == paper and computer == rock) or (user == scissors and computer == paper):
  print("Kamu menang!")
else:
  print("Kamu kalah!")


