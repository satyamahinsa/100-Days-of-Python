tinggi_siswa = input("Masukkan sebuah list tinggi badan siswa: ").split()

for n in range(0, len(tinggi_siswa)):
  tinggi_siswa[n] = int(tinggi_siswa[n])
print(tinggi_siswa)

banyak_siswa = 0
jumlah_tinggi_siswa = 0
for tinggi in tinggi_siswa:
  banyak_siswa += 1
  jumlah_tinggi_siswa += tinggi

rata_rata_tinggi_siswa = round(jumlah_tinggi_siswa / banyak_siswa)
print(rata_rata_tinggi_siswa)