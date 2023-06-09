# Day 2 - Memahami Tipe Data dan Memanipulasi Sebuah String

## 1. Tipe Data Primitif
Tipe data dasar yang terkenal dan perlu diketahui di Python, antara lain **string**, **integer**, **float**, dan **boolean**.

### String
String merupakan kumpulan karakter yang diapit oleh tanda `""` (petik dua) dalam membuatnya. Setiap karakter bisa diambil dengan menambahkan tanda `[]` (kurung siku) setelahnya dan di dalamnya berisi angka sebagai indeks karakter yang ingin diambil. **Penting untuk diingat bahwa indeks selalu dimulai dari 0 yang menyatakan posisi pertama** karena komputer bekerja dengan biner, yaitu 0 dan 1.

```python
print("Hello"[0]) // mencetak H sebagai indeks pertama dalam string tersebut
print("Hello"[4]) // mencetak o sebagai indeks terakhir dalam string tersebut
```

### Integer
Integer merupakan bilangan bulat. Tentunya, bilangan yang tanpa adanya penempatan desimal di dalamnya. 

```python
print(123 + 345) // mencetak hasil penjumlahan, yaitu 468
```

Dalam penulisan angka yang besar, seperti 12345678 bisa menggunakan tanda `_` (underscore) di antara ribuan agar memudahkan dalam pembacaannya. Nantinya, komputer akan menghapus dan mengabaikan tanda `_` tersebut.

### Float
Float merupakan bilangan desimal. Floating Point Number dapat terjadi karena titik desimal dapat ditempatkan sekitar bilangan tersebut.

```python
print(3.14159) // mencetak PI, yaitu 3,14159
```

### Boolean
Boolean terdiri dari 2 nilai, yaitu `True` berarti benar atau `False` berarti salah. **Penting untuk diingat bahwa kedua nilai diawali oleh huruf kapital dan tidak ada tanda petik dua yang mengapitnya**. Tipe data ini akan banyak digunakan dalam pemrograman untuk mengecek kebenaran sesuatu.

```python
print(True)
print(False)
```

## 2. Pengecekan & Konversi Tipe Data

### Mengecek Tipe Data Sebuah Variabel
Pengecekan tipe data bisa menggunakan `type()`. Pada dasarnya, fungsi ini akan mengecek tipe data pada variabel ataupun data yang diletakkan di antara tanda `()` (kurung).

```python
a = "Satya"
type(a) # <class 'str'>
type(15) # <class 'int'>
```

### Konversi Tipe Data Sebuah Variabel
Konversi dilakukan untuk mengubah tipe data tertentu sebuah variabel ke tipe data lainnya. Terdapat beberapa fungsi konversi di Python, antara lain `str()`, `int()`, `float()`. Di antara tanda `()` (kurung) memerlukan sebuah data atau variabel yang ingin diubah tipe datanya.

```python
a = 123
str(a) # mengubah int menjadi str
float(a) # mengubah int mnejadi float
```

## 3. Operasi Matematika di Python
Pada sebelumnya, kita melihat penggunaan tanda `+` (tambah) dalam menggabungkan sebuah kata atau sebagai operasi matematika. Selain tanda `+` (tambah), terdapat beberapa operasi matematika lainnya, antara lain `-` (kurang), `*` (kali), `/` (bagi), `%` (sisa hasil bagi), dan `**` (pangkat).

Fakta yang harus diketahui dalam melakukan operasi matematika sebagai berikut:
  - Pembagian selalu menghasilkan sebuah bilangan desimal (floating point number).
  - Adanya eksponen sebagai built-in di Python.
  - Jika memiliki 1 atau lebih operasi dalam 1 baris, maka terdapat tingkat prioritas tertentu. Prioritas pertama adalah `**`, `*` dan `/` menjadi prioritas kedua, lalu `+` dan `-` menjadi prioritas ketiga. 
  
```python
print(0 + 1) # 1
print(5 - 2) # 3
print(10 * 2) # 20
print(5 / 2) # 2.5
print(4 ** 3) # 64
```

## 4. Memanipulasi Bilangan dan Penggunaan f-String

### Pembulatan Bilangan
Di dalam python, implementasi pembulatan nilai bilangan sangat mudah dilakukan, yaitu menggunakan `round()`. Di dalam tanda `()` (kurung), kita bisa menambahkan operasi matematika dan juga presisi angka setelah koma.

```python
round(8 / 3, 2) # Pembulatan dengan presisi 2 angka di belakang koma menjadi 2,67.
```

Pembulatan ke bawah **(floor division)** bisa menggunakan tanda `//` di antara 2 bilangan. Hal ini memberikan hasil integer tanpa dilakukannya konversi lagi.

### Shorthand dalam Operasi Matematika
Berikut **shorthand** dalam melakukan operasi matematika:
  1. `a += 1` artinya `a = a + 1`.
  2. `a -= 1` artinya `a = a - 1`.
  3. `a *= 2` artinya `a = a * 2`.
  4. `a /= 2` artinya `a = a / 2`.

### Penggunaan f-String
**f-String** digunakan untuk memudahkan menggabungkan string dan tipe data lainnya. Semua konversi telah dilakukan secara otomatis untuk menjadi 1 string yang utuh.

```python
nama = "Gede"
skor = 0
menang = True
print(f"Hello, {nama}. Skor kamu adalah {skor}. Apakah kamu menang? {menang}")
```
