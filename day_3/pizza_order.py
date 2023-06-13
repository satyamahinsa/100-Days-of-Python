print("Selamat Datang di Python Pizza!")

# Meminta input dari user untuk ukuran, tambahan_pepperoni, dan ekstra_keju.
ukuran = input("Pilih ukuran pizza yang anda inginkan (S, M, L): ")
tambahan_pepperoni = input("Apakah anda ingin pepperoni? (Y/N): ")
ekstra_keju = input("Apakah anda ingin ekstra keju? (Y/N): ")
total_tagihan = 0

if ukuran == 'S':
  total_tagihan += 15000
elif ukuran == 'M':
  total_tagihan += 20000
else:
  total_tagihan += 25000

if tambahan_pepperoni == 'Y':
  if ukuran == 'S':
    total_tagihan += 2000
  else:
    total_tagihan += 3000

if ekstra_keju == 'Y':
  total_tagihan += 1000

print(f"Total tagihan anda: Rp. {total_tagihan}")