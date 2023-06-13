print("Pengecekan Tahun Kabisat")

# Meminta input dari user untuk memasukkan tahun yang ingin dicek.
year = int(input("Tahun: "))

if year % 4 == 0:
# Jika tahun tersebut habis dibagi 4, maka eksekusi kode berikut.
  if year % 100 == 0:
  # Jika tahun tersebut habis dibagi 4 dan 100, maka eksekusi kode berikut.
    if year % 400 == 0:
    # Jika tahun tersebut habis dibagi 4, 100, dan 400, maka tahun tersebut adalah tahun kabisat.
      print("Leap Year.")
    else:
    # Jika tahun tersebut habis dibagi 4 dan 100, tetapi tidak habis dibagi 400, maka tahun tersebut bukan tahun kabisat.
      print("Not Leap Year.")
  else:
  # Jika tahun tersebut habis dibagi 4, tetapi tidak habis dibagi 100, maka tahun tersebut adalah tahun kabisat.
    print("Leap Year.")
else:
# Jika tahun tersebut tidak habis dibagi 4, maka tahun tersebut bukan tahun kabisat.
  print("Not Leap Year.")