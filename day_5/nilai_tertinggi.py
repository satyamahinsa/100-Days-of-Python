nilai_siswa = input("Masukkan sebuah list nilai siswa: ").split()
for n in range(0, len(nilai_siswa)):
  nilai_siswa[n] = int(nilai_siswa[n])
print(nilai_siswa)

max = 0
for nilai in nilai_siswa:
  if nilai > max:
    max = nilai

print(f"Nilai tertinggi di kelas: {max}")