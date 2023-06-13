print("Selamat Datang di Dunia Bermain!")

# Meminta input dari pengunjung untuk tinggi dalam cm.
tinggi = int(input("Berapa tinggi kamu dalam cm?: "))

if tinggi >= 120:
  print("Kamu bisa masuk ke dalam Dunia Bermain! Nikmatilah permainan kami!")
  # Meminta input dari pengunjung untuk umur.
  umur = int(input("Berapa umur anda?: "))
  # Percabangan Bersarang
  if umur < 12:
    print("Harap membayar tiket masuk sebesar Rp. 5000")
  # Penggunaan elif
  elif umur <= 18:
    print("Harap membayar tiket masuk sebesar Rp. 7000")
  else:
    print("Harap membayar tiket masuk sebesar Rp. 12000")
else:
  print("Kamu tidak bisa masuk ke dalam Dunia Bermain! Mohon maaf!")
