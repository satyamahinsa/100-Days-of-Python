num_char = len(input("What's your name? "))

# Convert integer to string.
new_num_char = str(num_char)

print("Your name contains " + new_num_char + " characters.")

# Perform data type checking.
a = 123
print(type(a))

# There are 3 conversion functions:
str(a) # Convert to string.
int(a) # Convert to integer.
float(a) # Convert to float.

print(70 + float("100.5"))
print(str(70) + str(100))