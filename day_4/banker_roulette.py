import random

input_nama = input("Berikan saya nama semua orang, dipisahkan dengan koma. ")
kumpulan_nama = input_nama.split(", ")

nama = kumpulan_nama[random.randint(0, len(kumpulan_nama) - 1)]
print(f"Orang yang membayar tagihan: {nama}")

# Alternatif pemilihan data di dalam list secara random
nama = random.choice(kumpulan_nama)
print(f"Orang yang membayar tagihan: {nama}")
