num_char = len(input("What's your name? "))

# Konversi integer menjadi string.
new_num_char = str(num_char)

print("Your name contains " + new_num_char + " characters.")

# Melakukan pengecekan tipe data.
a = 123
print(type(a))

# Terdapat 3 fungsi konversi:
str(a) # Konversi menjadi string.
int(a) # Konversi menjadi integer.
float(a) # Konversi menjadi float.

print(70 + float("100.5"))
print(str(70) + str(100))