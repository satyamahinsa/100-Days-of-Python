# Requests input from the user to determine 
# whether the number is even or odd.
number = int(input("Number: "))

# Even numbers must be divisible by 2.
if number % 2 == 0:
  print(f"{number} is an even number.")
else:
  print(f"{number} is an odd number.")
