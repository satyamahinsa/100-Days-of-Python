import random
huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Selamat Datang di PyPassword Generator!")
banyak_huruf = int(input("Berapa banyak huruf yang Anda inginkan dalam kata sandi Anda?\n")) 
banyak_simbol = int(input(f"Berapa banyak simbol yang Anda inginkan?\n"))
banyak_angka = int(input(f"Berapa banyak angka yang Anda inginkan?\n"))

# Easy Version
password = ""
for char in range(0, banyak_huruf):
  password += random.choice(huruf)

for char in range(0, banyak_simbol):
  password += random.choice(simbol)

for char in range(0, banyak_angka):
  password += random.choice(angka)

print(f"Ini password kamu (Easy Version): {password}")

# Hard Version
password_list = []

for char in range(0, banyak_huruf):
  password_list.append(random.choice(huruf))
  
for char in range(0, banyak_simbol):
  password_list.append(random.choice(simbol))
  
for char in range(0, banyak_angka):
  password_list.append(random.choice(angka))

random.shuffle(password_list)

random_password = ""
for char in password_list:
  random_password += char

print(f"Ini password kamu (Hard Version): {random_password}")