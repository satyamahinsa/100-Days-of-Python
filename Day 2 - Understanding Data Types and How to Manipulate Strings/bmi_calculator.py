# Requests height and weight input from the user.
height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

# Perform the following operations to get the result_bmi.
result_bmi = float(weight) / float(height) ** 2

# Print result_bmi with integer data type.
print(int(result_bmi))