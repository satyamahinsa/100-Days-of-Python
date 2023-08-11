print("Welcome to the World of Play!")

# Request input from visitors for height in cm.
height = int(input("How tall are you in cm?:"))

if height >= 120:
  print("You can enter the World of Play! Enjoy our games!")
  # Requests input from the visitor for age.
  age = int(input("How old are you?:"))
  # Nested branching
  if age < 12:
    print("Please pay the entrance fee of Rp. 5000")
  # Use of elif
  elif age <= 18:
    print("Please pay the entrance fee of Rp. 7000")
  else:
    print("Please pay the entrance fee of Rp. 12000")
else:
  print("You cannot enter the World of Play! Sorry!")