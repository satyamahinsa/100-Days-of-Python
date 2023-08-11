# ASCII ART
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find a treasure.")

# Give the first choice to the user. The user is prompted to enter his/her choice.
choice1 = input("You are at a crossroads. Where do you want to go? Type 'left' or 'right'.\n").lower()
if choice1 == "left":
  # Provide the second choice to the user. The user is asked to enter his/her choice.
  choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n").lower()
  if choice2 == "wait":
    # Give the third choice to the user. The user is asked to enter his/her choice.
    choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? Type `red`, `yellow`, or `blue`.\n").lower()
    if choice3 == "red":
      print("This is a room full of fire. Game over!")
    elif choice3 == "blue":
      print("You are entering a room full of wild animals. Game over!")
    elif choice3 == "yellow":
      print("You found the treasure! You won!!!")
    else:
      print("You chose a door that doesn't exist. Game over!")
  else:
    print("You were attacked by an angry shark. Game over!")
else:
  print("You fell into a hole. Game over!")