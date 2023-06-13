print("Selamat Datang di Kalkulator Cinta!")

# Meminta input dari user untuk nama1 dan nama2
# lower() => digunakan untuk mengubah semua huruf di dalam string menjadi huruf kecil.
nama1 = input("Siapa nama anda?: ").lower()
nama2 = input("Siapa nama pasangan anda?: ").lower()

# Deklarasi variabel gabungan_nama untuk menggabungkan nama1 dan nama2.
gabungan_nama = nama1 + nama2

# Menghitung banyaknya kemunculan setiap huruf pada kata TRUE di kedua nama.
hitung_t = gabungan_nama.count('t')
hitung_r = gabungan_nama.count('r')
hitung_u = gabungan_nama.count('u')
hitung_e = gabungan_nama.count('e')

# Menghitung banyaknya kemunculan setiap huruf pada kata LOVE di kedua nama.
hitung_l = gabungan_nama.count('l')
hitung_o = gabungan_nama.count('o')
hitung_v = gabungan_nama.count('v')
hitung_e = gabungan_nama.count('e')

# Menghitung total nilai pada kata TRUE dan LOVE.
total_true = hitung_t + hitung_r + hitung_u + hitung_e
total_love = hitung_l + hitung_o + hitung_v + hitung_e

total_skor = int(str(total_love) + str(total_love))

if total_skor < 10 or total_skor > 90:
  print(f"Total skor adalah {total_skor}, hubungan kalian seperti cola dan mentos.")
elif total_skor > 40 and total_skor < 50:
  print(f"Total skor adalah {total_skor}, hubungan kalian baik selamanya.")
else:
  print(f"Total skor adalah {total_skor}.")