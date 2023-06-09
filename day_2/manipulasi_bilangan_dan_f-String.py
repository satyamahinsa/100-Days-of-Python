# Pembulatan bilangan menggunakan round().
# round() akan membulatkan secara otomatis (ke bawah atau ke atas) tergantung nilai di belakang koma.
result = round(8 / 3, 2)
print(result)

# Pembulatan bilangan menggunakan // (floor division).
# // akan membulatkan ke bawah.
result = 8 // 3
print(result)

# Penggunaan shorthand di Python
skor = 0
skor += 5
skor -= 1
skor *= 2
skor /= 4
print(skor)

# Penggunaan f-String.
nama = "Gede"
skor = 0
menang = True
print(f"Hello, {nama}. Skor kamu adalah {skor}. Apakah kamu menang? {menang}")