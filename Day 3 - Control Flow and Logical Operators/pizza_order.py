print("Welcome to Python Pizza!")

# Requests user input for size, extra_pepperoni, and extra_cheese.
size = input("Select your desired pizza size (S, M, L): ")
extra_pepperoni = input("Do you want pepperoni? (Y/N): ")
extra_cheese = input("Do you want extra cheese? (Y/N): ")
total_bill = 0

if size == 'S':
  total_bill += 15000
elif size == 'M':
  total_bill += 20000
else:
  total_bill += 25000

if extra_pepperoni == 'Y':
  if size == 'S':
    total_bill += 2000
  else:
    total_bill += 3000

if extra_cheese == 'Y':
  total_bill += 1000

print(f"Your total bill: Rp. {total_bill}")