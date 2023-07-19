# Hangman Project

## 1. Langkah-Langkah yang Diperlukan

1. Membuat kata acak.
2. Ganti kata tersebut dengan kosong "_" yang nantinya ditampilkan ke user.
3. Tanya user untuk menebak huruf tersebut.
4. Apakah tebakan huruf oleh user ada di dalam kata tersebut?
5. Jika tebakan user benar, maka ganti kosong "_" pada kata menjadi huruf yang ditebak oleh user secara bersesuaian.
   - Apakah semua kosong "_" pada user telah terisi semua? 
   - Jika iya, maka permainan selesai dan user menang karena sudah menebak semua huruf dengan tepat.
   - Jika tidak, maka kembali lagi ke langkah 3 dan selanjutnya.
6. Jika tebakan user salah, maka user kehilangan 1 nyawa dan menggambar figur hangman secara bertahap.
   - Apakah user sudah kehabisan nyawa (figur hangman sudah tergambar sepenuhnya)?
   - Jika iya, maka permainan selesai dan user kalah karena tidak menebak kata dengan benar dan kehabisan nyawa.
   - Jika tidak, maka kembali lagi ke langkah 3 dan selanjutnya.

## 2. Challenge 1 - Memilih Kata Secara Acak dan Memeriksa Jawaban

1. Secara acak memilih sebuah kata dari `kata_hewan` dan memasukkannya ke dalam sebuah variabel bernama `kata_terpilih`. Gunakan modul `random` untuk memilih kata yang tersedia secara acak. 
   ```python
   import random

   kata_hewan = ["banteng", "cendrawasih", "domba", "harimau", "kangguru"]
   kata_terpilih = random.choice(kata_hewan)
   ```

2. Tanya user untuk menebak sebuah huruf dan masukkan jawaban mereka ke dalam sebuah variabel bernama `tebakan_user`. Variabel tersebut dibuat semua huruf kecil dengan fungsi `lower()`.
   ```python
   print("Tema Kata adalah hewan")
   tebakan_user = input("Tebak sebuah huruf: ").lower()
   ```

3. Periksa apakah huruf yang ditebak oleh user merupakan salah satu huruf yang ada di dalam variabel `kata_terpilih`.
   ```python
   for huruf in kata_terpilih:
    if tebakan_user == huruf:
      print("Benar")
    else:
      print("Salah")
   ```

## 3. Challenge 2 - Mengganti Kosong "_" dengan Tebakan User

1. Buat sebuah list kosong dengan nama `hasil_tebakan_user`. Pada setiap huruf yang ada di dalam variabel `kata_terpilih`, tambahkan `_` ke dalam `hasil_tebakan_user`. Jadi, jika `kata_terpilih` adalah domba, maka `hasil_tebakan_user` seharusnya menjadi `["_", "_", "_", "_", "_"]` dengan 5 buah `_` yang merepresentasikan setiap huruf.
   ```python
   hasil_tebakan_user = []
   for n in range(len(kata_terpilih)):
    hasil_tebakan_user.append("_")
   ```

2. Lakukan perulangan yang melalui setiap posisi dalam variabel `kata_terpilih`. Jika huruf pada posisi tersebut sama dengan `tebakan_user`, maka tampilkan huruf tersebut pada `hasil_tebakan_user` sesuai dengan posisinya.
   ```python
   for posisi in range(len(kata_terpilih)):
    huruf = kata_terpilih[posisi]
    if tebakan_user == huruf:
      hasil_tebakan_user[posisi] = huruf
   ```

3. Tampilkan `hasil_tebakan_user` dan dapat terlihat huruf yang ditebak berada pada posisi yang benar.
   ```python
   print(hasil_tebakan_user)
   ```

## 4. Challenge 3 - Memeriksa Apakah Pemain Sudah Menang

1. Menggunakan while loop untuk membiarkan user menebak lagi. Perulangan harus berhenti ketika user telah menebak semua huruf yang ada di dalam `kata_terpilih` dan `hasil_tebakan_user` tidak mempunyai kosong lagi `_`. Lalu, beritahu user menang.
   ```python
   while "_" in hasil_tebakan_user:
      tebakan_user = input("Tebak sebuah huruf: ").lower()

      for posisi in range(len(kata_terpilih)):
         huruf = kata_terpilih[posisi]
         if tebakan_user == huruf:
            hasil_tebakan_user[posisi] = huruf

      print(hasil_tebakan_user)
   else:
      print("Kamu menang!")
   ```

## 5. Challenge 4 - Melacak Nyawa User Hingga Permainan Berakhir

1. Membuat sebuah variabel bernama `sisa_nyawa` untuk melacak sisa nyawa yang dimiliki oleh user. `sisa_nyawa` memiliki nilai awal, yaitu 6.
   ```python
   sisa_nyawa = 6
   ```
2. Jika `tebakan_user` merupakan huruf yang tidak ada dalam `kata_terpilih`, maka kurangi `sisa_nyawa` dengan 1. Kemudian, jika sisa nyawa sudah mencapai 0, maka permainan harus berakhir dan menampilkan pesan bahwa user kalah.
   ```python
   if tebakan_user not in kata_terpilih:
      sisa_nyawa -= 1
      if sisa_nyawa < 0:
         print("Kamu kalah")
         break
   ```
3. Menampilkan ASCII art dari `stages` yang sesuai dengan nilai `sisa_nyawa` saat ini.
   ```python
   print(stages[sisa_nyawa])
   ```

## 6. Challenge 5 - Meningkatkan Pengalaman Pengguna

1. Impor `logo` dari `hangman_art.py` dan cetak di awal permainan.
   
   ```python
   from hangman_art.py import logo
   print(logo)
   ```

2. Impor `stages` dari `hangman_art.py` pada setiap perulangan.
   
   ```python
   from hangman_art.py import stages
   print(stages[sisa_nyawa])
   ```

3. Jika user telah memasukkan huruf yang telah mereka tebak, cetak huruf tersebut dan beritahukan kepada mereka.
   ```python
   if tebakan_user in hasil_tebakan_user:
      print(f"Kamu sudah menebak {tebakan_user}")
   ```

4. Jika user telah memasukkan huruf yang telah mereka tebak, cetak huruf tersebut dan beritahukan kepada mereka.

   ```python
   if tebakan_user not in kata_terpilih:
      print(f"Anda menebak {tebakan_user}, itu tidak ada dalam kata. Anda kehilangan 1 nyawa.")
      sisa_nyawa -= 1
      if sisa_nyawa < 0:
         print("Kamu kalah")
         break
   ```

## 7. Keseluruhan Hasil Program Hangman Project

```python
import random
from hangman_art import logo, stages

kata_hewan = ["banteng", "cendrawasih", "domba", "harimau", "kangguru"]

kata_terpilih = random.choice(kata_hewan)
sisa_nyawa = 6

hasil_tebakan_user = []
for n in range(len(kata_terpilih)):
   hasil_tebakan_user.append("_")

print(logo)
print("Tema Kata adalah Hewan")

while "_" in hasil_tebakan_user:
   tebakan_user = input("Tebak sebuah huruf: ").lower()

   if tebakan_user in hasil_tebakan_user:
      print(f"Kamu sudah menebak {tebakan_user}")

   for posisi in range(len(kata_terpilih)):
      huruf = kata_terpilih[posisi]
      if tebakan_user == huruf:
         hasil_tebakan_user[posisi] = huruf

   if tebakan_user not in kata_terpilih:
      print(f"Anda menebak {tebakan_user}, itu tidak ada dalam kata. Anda kehilangan 1 nyawa.")
      sisa_nyawa -= 1
      if sisa_nyawa == 0:
         print("Kamu kalah")
         break

   print(f"{' '.join(hasil_tebakan_user)}")
   print(stages[sisa_nyawa])
else:
   print("Kamu menang!")

print(stages[sisa_nyawa])
```