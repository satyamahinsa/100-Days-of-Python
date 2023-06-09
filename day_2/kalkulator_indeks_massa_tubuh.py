# Meminta input tinggi dan berat badan dari user.
tinggi = input("Masukkan tinggi anda dalam meter: ")
berat = input("Masukkan berat anda dalam kilogram: ")

# Melakukan operasi berikut untuk mendapatkan hasil_indeks_massa_tubuh.
hasil_indeks_massa_tubuh = float(tinggi) / float(berat) ** 2

# Mencetak hasil_indeks_massa_tubuh dengan tipe data integer.
print(int(hasil_indeks_massa_tubuh))