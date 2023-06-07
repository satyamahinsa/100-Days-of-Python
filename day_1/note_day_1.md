# Day 1 - Bekerja dengan Variabel untuk Mengelola Data

## 1. Mencetak ke Konsol
Cara kerja `print()` sangat sederhana. Di dalam tanda kurung, anda memberitahu apa yang ingin dicetak ke konsol. Fungsi ini menerima semua tipe data yang ada di Python.

```python
print("Hello World!") // mencetak string Hello World!
```

## 2. Tipe Data String
**String** merupakan tipe data yang terdiri dari serangkaian karakter dan diapit oleh petik dua sebagai awal dan akhir dari serangkaian karakter tersebut.

```python
"Halo, nama saya Putu"
"Tes123"
```

Beberapa cara memanipulasi string:
  1. Membuat baris baru dengan menggunakan `\n`.
      ```python
      print("Hello World!\nHello World!\nHello World!")
      // Hello World!
      // Hello World!
      // Hello World!
      ```
  2. Menggabungkan 2 atau lebih serangkaian kata atau kalimat menjadi 1 kalimat utuh dengan menggunakan `+`.
      ```python
      print("Hello" + " " + "Satya") // Hello Satya
      // NOTE: di dalam Python, spasi sangatlah penting. 
      ``` 

## 3. Mengambil Data dari User
`input()` digunakan untuk mengambil data yang dimasukkan oleh user melalui konsol. Setelah `input()` dieksekusi, maka kursor akan berada di akhir dari baris dan menunggu masukan dari user. Cara kerjanya adalah masukan dari user akan mengganti bagian dari `input()` yang memintanya. 

```python
input("What's your name? ")
print("Hello, " + input("What's your name? "))
```

Perbedaan antara `print()` dan `input()` adalah `print()` akan mengakhiri eksekusi kode setelahnya, sedangkan `input()` akan menunggu masukan dari user yang nantinya kan 

## 4. Membuat Comment di Python

Baris teks yang diabaikan atau tidak dieksekusi oleh Python disebut **comment**. Cara membuatnya adalah dengan menambahkan `#` di awal baris.

```python
# Ini adalah sebuah contoh comment.
```

Fungsi dari **comment** adalah memberikan penjelasan suatu kode yang telah dibuat agar dapat dipahami oleh diri sendiri maupun orang lain yang membaca kode tersebut.

Cara cepat mengubah baris kode menjadi **comment** adalah `Ctrl + /` 

## 5. Variabel di Python
**Variabel** digunakan untuk menyimpan sebuah nilai atau data. Data yang ada di dalam variabel bisa diubah kapan saja. Penamaan sebuah variabel harus sesuai dengan isi dari data agar dapat dengan mudah dipahami.

```python
nama = "Gede Satyamahinsa"
umur = 19
```

Beberapa hal yang harus dihindari dalam penamaan sebuah variabel, antara lain:
   1. Tidak menggunakan spasi dalam memisahkan kata dalam kalimat. Sebagai gantinya bisa menggunakan `_` (underscore). Contoh: `user_name`, `data_barang`, `umur_saat_ini`.
   2. Tidak menggunakan angka di awal nama variabel, tetapi boleh menggunakannya di akhir.. Contoh: `num1`, `produk2`, `rumah3`.
   3. Tidak menggunakan nama built-in function, seperti `print()`, `input()`, dll sebagai nama dari variabel. Hal ini diterapkan agar tidak ada kekeliruan dalam penggunaannya nanti.