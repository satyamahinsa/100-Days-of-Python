# ASCII ART
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Selamat Datang di Pulau Harta Karun!")
print("Misi anda adalah menemukan sebuah harta karun.")

# Memberikan pilihan pertama kepada user. User diminta untuk memasukkan pilihannya.
pilihan1 = input("Anda berada di persimpangan jalan. Kemana anda ingin pergi? Ketik 'kiri' atau 'kanan'.\n").lower()
if pilihan1 == "kiri":
  # Memberikan pilihan kedua kepada user. User diminta untuk memasukkan pilihannya.
  pilihan2 = input("Anda telah datang ke sebuah danau. Ada sebuah pulau di tengah danau. Ketik 'tunggu' untuk menunggu perahu. Ketik 'berenang' untuk berenang menyeberang.\n").lower()
  if pilihan2 == "tunggu":
    # Memberikan pilihan ketiga kepada user. User diminta untuk memasukkan pilihannya.
    pilihan3 = input("Anda tiba di pulau dengan kondisi tanpa cedera. Ada sebuah rumah dengan 3 pintu. Satu merah, satu kuning dan satu biru. Warna mana yang Anda pilih? Ketik `merah`, `kuning`, atau `biru`.\n").lower()
    if pilihan3 == "merah":
      print("Ini adalah ruangan yang penuh dengan api. Permainan berakhir!")
    elif pilihan3 == "biru":
      print("Anda memasuki ruangan yang penuh dengan binatang buas. Permainan berakhir!")
    elif pilihan3 == "kuning":
      print("Anda menemukan harta karunnya! Anda menang!!!")
    else:
      print("Anda memilih pintu yang tidak ada. Permainan berakhir!")
  else:
    print("Anda diserang oleh ikan hiu yang marah. Permainan berakhir!")
else:
  print("Anda jatuh ke dalam lubang. Permainan berakhir!")
  