# Meminta input dari user untuk umur saat ini.
umur = input("Berapa umur kamu saat ini? ")

# Menghitung sisa umur jika kita hidup sampai 90 tahun.
sisa_umur = 90 - int(umur)
sisa_hari = 365 * sisa_umur
sisa_minggu = 52 * sisa_umur
sisa_bulan = 12 * sisa_umur

# Mencetak pesan yang dinginkan.
print(f"You have {sisa_hari} days, {sisa_minggu} weeks, and {sisa_bulan} months left")