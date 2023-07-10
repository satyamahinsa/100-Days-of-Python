# ----------- BLOK FUNGSI ------------
def tebakWarna():
  buah = input("Tuliskan nama buah: ")
  # ----- BLOK IF -----
  if buah == "anggur":
    print("Ungu.")
  # -------------------
  # ----- BLOK ELIF -----
  elif buah == "jeruk":
    print("Orange.")
  # ---------------------
  # ----- BLOK ELSE -----
  else:
    print("Buah selain anggur dan jeruk.")
  # ---------------------

tebakWarna()