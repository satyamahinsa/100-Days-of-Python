print("Leap Year Checking")

# Requests input from the user to enter the year to be checked.
year = int(input("Year: "))

if year % 4 == 0:
# If the year is divisible by 4, then execute the following code.
  if year % 100 == 0:
  # If the year is divisible by 4 and 100, then execute the following code.
    if year % 400 == 0:
    # If the year is divisible by 4, 100, and 400, then the year is a leap year.
      print("Leap Year.")
    else:
    # If the year is divisible by 4 and 100, but not by 400, then the year is not a leap year.
      print("Not Leap Year.")
  else:
  # If the year is divisible by 4, but not divisible by 100, then the year is a leap year.
    print("Leap Year.")
else:
# If the year is not divisible by 4, then the year is not a leap year.
  print("Not Leap Year.")