print("Selamat Datang di Dunia Bermain!")

# Meminta input dari pengunjung untuk tinggi dalam cm.
tinggi = int(input("Berapa tinggi kamu dalam cm?: "))
tagihan = 0

if tinggi >= 120:
  print("Kamu bisa masuk ke dalam Dunia Bermain! Nikmatilah permainan kami!")
  # Meminta input dari pengunjung untuk umur.
  umur = int(input("Berapa umur anda?: "))
  # Percabangan Bersarang
  if umur < 12:
    print("Harap membayar tiket masuk sebesar Rp. 5000")
    tagihan = 5000
  # Penggunaan elif
  elif umur <= 18:
    print("Harap membayar tiket masuk sebesar Rp. 7000")
    tagihan = 7000
  else:
    print("Harap membayar tiket masuk sebesar Rp. 12000")
    tagihan = 12000
  
  # Meminta input dari pengunjung untuk tambahan biaya foto.
  biaya_foto = input("Apakah anda ingin diambil fotonya? (Y/N): ")
  
  # Penggunaan multiple if statement.
  if biaya_foto == 'Y':
    tagihan += 3000
  
  # Mencetak total tagihan yang harus dibayarkan oleh pengunjung.
  print(f"Total tagihan anda: Rp. {tagihan}")
else:
  print("Kamu tidak bisa masuk ke dalam Dunia Bermain! Mohon maaf!")
