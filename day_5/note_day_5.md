# Perulangan di Python

## 1. Penggunaan for loop dengan List

Perulangan for loop mudah dikombinasikan dengan list. Dengan menggunakan for loop, kita bisa melalui setiap elemen dan melakukan sebuah aksi terhadapnya secara individu.

```python
hewan_berkaki_empat = ["Sapi", "Anjing", "Kucing"]

# Perulangan berikut dieksekusi sebanyak jumlah elemen yang ada di dalam list.
for hewan in hewan_berkaki_empat:
  # Setiap elemen akan berada di variabel hewan secara bergantian.
  print(hewan) # Menampilkan setiap elemen yang ada di dalam list hewan_berkaki_empat.
print(hewan_berkaki_empat) # Kode ini dieksekusi 1 kali karena berada di luar for loop.
```

**Aspek penting dalam perulangan** adalah memungkinkan kita untuk mengeksekusi seluruh baris kode yang sama dalam beberapa kali secara berulang. Penting untuk diingat bahwa baris kode yang ingin dieksekusi harus berada di dalam for loop (adanya indentasi atau tab)

## 2. Penggunaan for loop dengan fungsi range()

`range()` adalah fungsi untuk menghasilkan bilangan pada rentang tertentu. Fungsi ini mempunyai 2 parameter wajib dan 1 parameter opsional. 

**NOTASI**: `range(bilangan awal, bilangan akhir, [opsional: langkah])`
**NOTE**: bilangan akhir pada parameter bersifat tidak inklusif. Jadi, perlu ditambahkan 1 untuk mendapatkan bilangan akhir yang sesuai dan diinginkan.

```python
# Variabel angka digunakan untuk mengambil 1 elemen 
# yang dihasilkan oleh range() pada setiap perulangan. 
for angka in range(1, 11):
  print(angka) # Menampilkan setiap elemen pada perulangan, yaitu bilangan 1 sampai 10 (tidak termasuk 11).

for angka in range(1, 11, 2):
  print(angka) # Menampilkan semua bilangan ganjil dari 1 sampai 10.
  # Angka 2 pada parameter terakhir sebagai ukuran langkah setiap perulangan sebanyak 2 kali (default = 1).
```