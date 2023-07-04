# Modul Random dan List pada Python

## 1. Apa itu Modul?
Sebagian besar, kita menulis kode di dalam 1 file yang sama dan dieksekusi dari atas ke bawah.

Terkadang, kode yang kita buat bisa sangat panjang dan sangat sulit untuk dipahami. Dalam kasus seperti ini, kita dapat memisahkan kode yang begitu panjang menjadi beberapa modul. **Setiap modul memiliki fungsi yang berbeda-beda**.

 - Cara membuat modul di Python adalah membuat file berbeda, selain file utama yang akan dieksekusi.

 - Cara menambahkan modul ke dalam file utama adalah menggunakan kata kunci `import` di bagian baris paling atas kode kita.

## 2. Modul Random
Di Python, terdapat modul yang telah dibuat oleh Python itu sendiri untuk memudahkan dalam menghasilkan bilangan acak semu, yaitu `random`. `random` memiliki banyak fungsi di dalamnya yang memungkinkan untuk menghasilkan bilangan bulat atau desimal secara acak.

Terdapat beberapa fungsi penting di dalam modul `random` sebagai berikut:
| Kode | Fungsi |
| ---- | ------ |
| `randrange(start, stop, step)` | Mengembalikan bilangan bulat yang dipilih secara acak dimulai dari `start` hingga `stop` dengan kelipatan `step` |
| `randint(start, stop)` | Mengembalikan bilangan bulat acak di antara `start` dan `stop` (inklusif) |
| `random()` | Mengembalikan bilangan desimal (floating point number) di antara 0.000... hingga 0.999... [0.0 hingga 1.0) |

```python
import random

print(random.randint(1, 10))
print(random.randrange(1, 10, 2))
print(random.random()) * 5 # Mengembalikan bilangan desimal antara [0.0 hingga 5.0)
```

## 3. Apa itu List?
List merupakan struktur data yang digunakan sebagai cara untuk mengatur dan menyimpan data di Python. Struktur data ini bisa menyimpan banyak data yang mempunyai hubungan antar sesamanya.List bisa menyimpan banyak data dengan berbagai tipe data

Berikut sintaks dalam pembuatan list pada Python:
```python
data = [item1, item2, item3]
```

Penting untuk diingat bahwa list mempunyai urutan data yang menentukan urutannya di dalam list. Urutan ini digunakan untuk mengakses data di dalamnya. Dalam mengakses data, kita perlu menggunakan `[]` sebagai indeks. Data pertama dalam list diakses menggunakan indeks 0. **Mengapa indeks dimulai dari 0?** karena adanya pergeseran akses dari awal list. Misalnya, data kedua menggunakan indeks 1 karena adanya pergeseran sebanyak 1 kali dari awal list.  

```python
hewan = ["Kucing", "Kuda", "Semut"]

hewan[0] # mengakses indeks pertama
hewan[-1] # mengakses indeks terakhir
hewan[-2] # mengakses indeks kedua terakhir
```

Data di dalam list bisa diubah dengan memasukkan data baru ke dalamnya.

```python
makanan = ["Pizza", "Donat", "Nasi Goreng"]

makanan[1] = "Kue Bolu" # mengubah data pada indeks 1 menjadi Kue Bolu
```

Banyak fungsi built-in yang ada di dalam list. Berikut beberapa penjelasan fungsi tersebut:

```python
minuman = ["Coca Cola", "Jamu", "Aqua"]

minuman.append("Yogurt") # menambahkan Yogurt ke akhir list
minuman.extend(["Teh", "Kopi"]) # menambahkan banyak data ke akhir list
```

## List Bersarang
List bersarang **(Nested Lists)** adalah list yang ada di dalam list. Hal ini banyak digunakan dalam menulis kode di Python. Kegunaan list bersarang adalah membedakan beberapa data ke dalam sebuah list (kategori), namun masih ada keterkaitan antar satu sama lain.

```python
makanan = ["Sate Ayam", "Nasi Goreng", "Sayur Sop"]
minuman = ["Air Putih", "Teh", "Es Jeruk"]

kebutuhan = [makanan, minuman]
# [["Sate Ayam", "Nasi Goreng", "Sayur Sop"], ["Air Putih", "Teh", "Es Jeruk"]]
```
