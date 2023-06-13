# Meminta input dari user untuk menentukan 
# apakah angka tersebut genap atau ganjil.
angka = int(input("Angka: "))

# Bilangan genap pasti habis dibagi 2.
if angka % 2 == 0:
  print(f"{angka} termasuk bilangan genap.")
else:
  print(f"{angka} termasuk bilangan ganjil.")
