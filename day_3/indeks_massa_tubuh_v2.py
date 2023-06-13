# Meminta input tinggi dan berat badan dari user.
tinggi = float(input("Masukkan tinggi anda dalam meter: "))
berat = float(input("Masukkan berat anda dalam kilogram: "))

# Melakukan operasi berikut untuk mendapatkan hasil_indeks_massa_tubuh.
hasil_indeks_massa_tubuh = round(float(berat) / float(tinggi) ** 2)

# Mencetak hasil_indeks_massa_tubuh dan interpretasinya sesuai dengan hasil tersebut.
if hasil_indeks_massa_tubuh < 18.5:
  print(f"Indeks Massa Tubuh anda adalah {hasil_indeks_massa_tubuh}, kamu kekurangan berat badan.")
elif hasil_indeks_massa_tubuh < 25:
  print(f"Indeks Massa Tubuh anda adalah {hasil_indeks_massa_tubuh}, kamu memiliki berat badan normal.")
elif hasil_indeks_massa_tubuh < 30:
  print(f"Indeks Massa Tubuh anda adalah {hasil_indeks_massa_tubuh}, kamu kelebihan berat badan.")
elif hasil_indeks_massa_tubuh < 35:
  print(f"Indeks Massa Tubuh anda adalah {hasil_indeks_massa_tubuh}, kamu mengalami obesitas.")
else:
  print(f"Indeks Massa Tubuh anda adalah {hasil_indeks_massa_tubuh}, kamu mengalami obesitas secara klinis.")