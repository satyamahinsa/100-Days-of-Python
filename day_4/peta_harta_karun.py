baris1 = ['🟥', '🟥', '🟥']
baris2 = ['🟥', '🟥', '🟥']
baris3 = ['🟥', '🟥', '🟥']

peta = [baris1, baris2, baris3]
print(f"{baris1}\n{baris2}\n{baris3}")

posisi_harta_karun = input("Di mana Anda ingin menaruh harta karun itu?: ")
kolom = int(posisi_harta_karun[0]) - 1
baris = int(posisi_harta_karun[1]) - 1

peta[baris][kolom] = '❎'
print(f"{baris1}\n{baris2}\n{baris3}")