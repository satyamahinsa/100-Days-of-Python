# Fungsi, Blok Kode, dan While Loop pada Python

## 1. Pengertian Fungsi pada Python

**Fungsi merupakan kumpulan baris kode atau perintah yang menjadi satu kesatuan untuk nantinya bisa dipanggil atau digunakan berkali-kali.** Fungsi dibuat pasti memiliki tujuan tertentu, salah satunya adalah memecah program atau masalah yang besar menjadi bagian-bagian yang lebih kecil dengan tugasnya masing-masing. Selain itu juga, fungsi membuat kode program menjadi lebih *reusable* dan terstruktur.

Sebuah fungsi bisa menerima parameter, bisa mengembalikan suatu nilai *(return value)*, dan bisa dipanggil berkali-kali secara independen.

## 2. Cara Membuat Sebuah Fungsi

Di dalam python, terdapat banyak fungsi built-in yang dapat digunakan, seperti `print()`, `input()`, `len()`, `int()`, dan masih banyak lagi. Ada 2 langkah dalam membuat fungsi yang kita inginkan, yaitu mendefinisikan fungsi untuk memberitahu apa saja yang harus dilakukan dan memanggil fungsi untuk dieksekusi.

Ada beberapa unsur penting yang harus diperhatikan dalam membuat fungsi, yaitu kata kunci `def`, nama fungsi yang diikuti dengan `()` dan parameter yang ada di dalam `()` bila diperlukan. Lalu, tuliskan kode di dalam fungsi yang nantinya akan ikut saat fungsi dipanggil.

```python
def namaFungsi():
  # Perintah yang ingin dijalankan saat fungsi dipanggil.
```

Ketika suatu fungsi ingin dieksekusi, maka kita perlu memanggil fungsi tersebut dengan cara mengetikkan nama fungsi yang diikuti dengan `()` dan argumen di dalamnya apabila diperlukan.

```python
# namaFungsi() dipanggil dan dieksekusi sebanyak 2 kali.
namaFungsi()
namaFungsi()
```

## 3. Indentasi pada Python

Indentasi sangat penting untuk diperhatikan pada Python. Pada umumnya, python menggunakan 4 spasi (geser ke kanan) yang menandakan indentasi. Sebagai contoh adalah fungsi, kode yang ada di dalam fungsi harus 4 spasi ke dalam agar kode tersebut dieksekusi saat fungsi dipanggil. Indentasi bisa menggunakan `tab` atau `spasi`.

```python
def fungsi():
    # 4 spasi ke dalam agar kode dieksekusi.
    print("Hello")
print("World!") # kode ini tidak akan dieksekusi karena dianggap berada di luar fungsi. 
```

```python

# ----- BLOK FUNGSI -----
def fungsi():
  # --- BLOK IF ---
  if buah == "Anggur":
    print("Ungu")
  # ----------------
  # --- BLOK ELIF ---
  elif buah == "Jeruk":
    print("Orange")
  # -----------------
  print("Hello")
# -----------------------
print("World!")
```

## 4. While Loop pada Python

**While Loop** merupakan perulangan yang akan berlanjut selama kondisi tertentu bernilai benar. Berbeda dengan for loop yang mendefinisikan banyak perulangan dilakukan di awal, while loop tidak memiliki batasan dalam perulangannya. Maka dari itu, diperlukannya suatu pernyataan agar kondisi bernilai salah. Dalam membuat while loop, diperlukan kata kunci `while` dan kondisi tertentu yang diikuti dengan `:`. Lalu, di dalam while loop, terdapat kumpulan perintah atau baris kode yang nantinya dieksekusi saat perulangan berlangsung.

```python
while kondisi:
  # Lakukan sesuatu secara berulang hingga kondisi bernilai salah.

batu = 5
while batu > 0:
  print("Lompat")
  batu -= 1
```

Perbedaan **for loop** dan **while loop** sebagai berikut:
  1. For loop sangat cocok digunakan untuk melakukan iterasi (perulangan) dan ingin melakukan sesuatu pada setiap elemennya. Pada for loop, kita mengatur banyak perulangan dilakukan.
  2. While loop sangat cocok digunakan ketika tidak ingin melakukan sesuatu pada setiap elemen dan hanya ingin melakukan sebuah fungsionalitas sebanyak mungkin hingga kondisi bernilai salah. Tetapi, perlu diingat bahwa while loop sedikit berbahaya karena bisa saja menyebabkan *infinite loop* (perulangan tak berhingga) karena kondisi terus bernilai benar