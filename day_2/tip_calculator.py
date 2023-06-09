print("Salamat Datang di Kalkulator Tip!")

# Meminta input dari user untuk total tagihan.
total_tagihan = int(input("Berapa total tagihan yang harus dibayar?: Rp. "))

# Meminta input dari user untuk persentase tip yang ingin diberikan.
persentase_tip = int(input("Berapa persentase tip yang ingin anda berikan? (10, 12, or 15): "))

# Meminta input dari user untuk banyak orang yang membayar tagihan + tip.
banyak_orang = int(input("Berapa banyak orang yang harus membayar tagihan?: "))

# Menghitung bayaran tagihan setiap orang.
tagihan_setiap_orang = (total_tagihan * (1 + persentase_tip / 100)) / banyak_orang

# Mencetak hasil perhitungan untuk bayaran tagihan setiap orang.
print(f"Each person should pay: Rp. {round(tagihan_setiap_orang)}")