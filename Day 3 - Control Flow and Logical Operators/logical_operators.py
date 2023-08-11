print("Welcome to the World of Play!")

# Request input from visitors for height in cm.
height = int(input("How tall are you in cm?:"))
bill = 0

if height >= 120:
  print("You can enter the World of Play! Enjoy our games!")
  # Requests input from the visitor for age.
  age = int(input("How old are you?:"))
  # Nested branching
  if age >= 45 and age <= 55:
    print("Special! You get a free ticket!")
  elif age < 12:
    print("Please pay the entrance fee of Rp. 5000")
    bill = 5000
  # Use of elif
  elif age <= 18:
    print("Please pay an entrance fee of Rp. 7000")
    bill = 7000
  else:
    print("Please pay the entrance fee of Rp. 12000")
    bill = 12000
  
  # Request input from visitors for additional photo fees.
  photo_fee = input("Would you like a photo taken? (Y/N): ")
  
  # Use of multiple if statements.
  if photo_fee == 'Y':
    bill += 3000
  
  # Print the total bill that must be paid by the visitor.
  print(f"Your total bill: Rp. {bill}")
else:
  print("You can't enter the World of Play! Sorry!")