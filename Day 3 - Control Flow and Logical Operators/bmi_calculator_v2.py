# Requests height and weight input from the user.
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Perform the following operation to get the result_bmi.
result_bmi = round(float(weight) / float(height) ** 2)

# Print the result_bmi and interpret it accordingly.
if result_bmi < 18.5:
  print(f"Your Body Mass Index is { result_bmi}, you are underweight.")
elif result_bmi < 25:
  print(f"Your Body Mass Index is {result_bmi}, you are of normal weight.")
elif result_bmi < 30:
  print(f"Your Body Mass Index is {result_bmi}, you are overweight.")
elif result_bmi < 35:
  print(f"Your Body Mass Index is {result_bmi}, you are obese.")
else:
  print(f"Your Body Mass Index is {result_bmi}, you are clinically obese.")