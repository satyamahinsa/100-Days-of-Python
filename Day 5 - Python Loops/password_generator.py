import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
many_letters = int(input("How many letters do you want in your password?")) 
many_symbols = int(input("How many symbols do you want?"))
many_numbers = int(input("How many numbers do you want?"))

# Easy Version
password = ""
for char in range(0, many_letters):
  password += random.choice(letters)

for char in range(0, many_symbols):
  password += random.choice(symbol)

for char in range(0, many_numbers):
  password += random.choice(number)

print(f"This is your password (Easy Version): {password}")

# Hard Version
password_list = []

for char in range(0, many_letters):
  password_list.append(random.choice(letters))
  
for char in range(0, many_symbols):
  password_list.append(random.choice(symbol))
  
for char in range(0, many_numbers):
  password_list.append(random.choice(number))

random.shuffle(password_list)

random_password = ""
for char in password_list:
  random_password += char

print(f"This is your password (Hard Version): {random_password}")