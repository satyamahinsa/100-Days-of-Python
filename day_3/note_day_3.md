# Day 3 - Alur Kontrol dan Operator Logika

## 1. Alur Kontrol dengan if / else dan Operator Kondisional

### Pernyataan Kondisional: if / else
`if` / `else` merupakan pernyataan yang bergantung pada sebuah kondisi tertentu dan nantinya mengeksekusi kode sesuai dengan nilai kebenaran kondisi tersebut. Dengan adanya `if` / `else`, kode dapat melakukan sesuatu atau memberikan respon yang berbeda tergantung dengan kondisi yang berbeda pula. 

```python
if kondisi:
  # jika kondisi bernilai benar, maka eksekusi kode berikut.
else:
  # jika kondisi bernilai salah, maka eksekusi kode berikut.
```

`kondisi` merupakan sesuatu yang dilakukan pengecekan terhadap pernyataan `if` / `else`. Blok kode yang dieksekusi tergantung nilai kebenaran dari `kondisi`. 

**NOTE**: **Indentasi (spasi atau tab)** sangat penting dan mempengaruhi eksekusi suatu program. Sebuah indentasi menunjukkan bahwa blok kode berada di dalam kode lainnya.

### Operator Perbandingan
Operator perbandingan digunakan untuk membandingkan 2 buah nilai. Hasil perbandingan tersebut bernilai boolean, yaitu `True` atau `False`. Terdapat 6 operator perbandingan di Python, antara lain:
  1. **Lebih besar** (>)
  2. **Lebih kecil** (<)
  3. **Lebih besar atau sama dengan** (>=)
  4. **Lebih kecil atau sama dengan** (<=)
  5. **Sama dengan** (==)
  6. **Tidak sama dengan** (!=)

```python
print(5 > 2) # True
print(10 < 6) # False
print(1 >= 1) # True
print(7 <= 2) # False
print(9 == 9) # True
print(1 != 3) # True
```

Perbedaan antara `=` dan `==` adalah `=` digunakan untuk menentapkan atau memberikan sebuah nilai ke dalam variabel, sedangkan `==` digunakan untuk mengecek kesamaan nilai antara 2 buah nilai.

## 2. Percabangan Bersarang dan Penggunaan elif

### Percabangan Bersarang
Percabangan bersarang adalah percabangan yang ada di dalam percabangan lainnya (if yang ada di dalam if lainnya). Alur kerjanya adalah mengecek kondisi pertama terlebih dahulu. Jika kondisi pertama bernilai `True`, maka masuk ke dalam pengecekan kondisi kedua yang ada di dalamnya, sedangkan jika kondisi pertama bernilai `False`, maka masuk ke dalam `else`. Begitupun seterusnya.

```python
if kondisi1:
  if kondisi2:
    # Jika kondisi1 dan kondisi2 keduanya benar, maka eksekusi kode berikut.
  else:
    # Jika kondisi1 benar dan kondisi2 salah, maka eksekusi kode berikut.
else:
 # Jika kondisi1 salah, maka eksekusi kode berikut.
```

### Penggunaan elif
`elif` digunakan untuk menambahkan kondisi sebanyak yang kita inginkan dalam sebuah percabangan. Cara kerjanya adalah jika kondisi pertama bernilai `False`, maka lanjut ke pengecekan kondisi kedua, yaitu `elif`. Begitupun seterusnya hingga mencapai `else` sebagai kode yang dieksekusi jika tidak ada kondisi yang memenuhi.

```python
if kondisi1:
  # Jika kondisi1 bernilai benar, maka eksekusi kode berikut.
elif kondisi2:
  # Jika kondisi2 bernilai benar, maka eksekusi kode berikut.
else:
  # Jika tidak ada kondisi yang memenuhi, maka eksekusi kode berikut.
```

### Penggunaan Multiple if Statement
Pada materi sebelumnya, terdapat `if`, `elif`, dan `else` yang digunakan untuk mengecek banyak kondisi, tetapi disini hanya mengecek 1 kondisi dari sekian banyak kondisi. Ketika ada kondisi bernilai benar, maka kondisi setelahnya tidak akan dicek atau dilewati begitu saja.

Multiple `if` digunakan untuk mengecek sebuah kondisi, walaupun pengecekan kondisi sebelumnya juga bernilai benar.

```python
if kondisi1:
  # Jika kondisi1 bernilai benar, maka eksekusi kode berikut.
if kondisi2:
  # Jika kondisi2 bernilai benar, maka eksekusi kode berikut.
if kondisi3:
  # Jika kondisi3 bernilai benar, maka eksekusi kode berikut.
```

**NOTE**: indentasi (spasi atau tab) sangat penting yang akan mempengaruhi jalannya eksekusi kode.

### Operator Logika

Materi sebelumnya, yaitu membahas mengenai pengecekan kondisi menggunakan `if` yang banyak dan berurutan.

**Bagaimana jika kita ingin mengecek banyak kondisi dalam 1 baris kode yang sama? Bagaimana cara mengkombinasikan kondisi yang begitu banyak?**

Nah, disinilah operator logika digunakan. **Operator logika** adalah operator yang digunakan untuk membandingkan 2 atau lebih kondisi. Operator ini memberikan hasil boolean, yaitu `True` atau `False`. Terdapat 3 jenis operator logika, antara lain:

  1. **and**
      Ketika 2 atau lebih kondisi menggunakan `and`, maka semua kondisi harus bernilai `True` untuk mendapatkan  hasil evaluasi bernilai `True`. Apabila terdapat salah satu kondisi bernilai `False`, maka hasil evaluasi bernilai `False`.

      **Tabel Kebenaran:**
      |   A   |   B   | A and B |
      | ----- | ----- | ------- |
      | True  | True  |  True   |
      | True  | False |  False  |
      | False | True  |  False  |
      | False | False |  False  |
      
  2. **or**
      Ketika 2 atau lebih kondisi menggunakan `or`, maka hanya dibutuhkan 1 kondisi saja bernilai `True` atau keduanya untuk mendapatkan hasil evaluasi bernilai `True`. Apabila semua kondisi bernilai `False`, maka hasil evaluasi bernilai `False`.

      **Tabel Kebenaran:**
      |   A   |   B   | A and B |
      | ----- | ----- | ------- |
      | True  | True  |  True   |
      | True  | False |  True   |
      | False | True  |  True   |
      | False | False |  False  |

  3. **not**
      `not` digunakan untuk membalikkan sebuah kondisi. Jika kondisi bernilai `True`, maka hasil evaluasei bernilai `False`. Begitupun sebaliknya. 

      **Tabel Kebenaran:**
      |   A   | not A |
      | ----- | ----- |
      | True  | False | 
      | True  | True  |