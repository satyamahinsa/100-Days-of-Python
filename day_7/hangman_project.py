import random
from hangman_art import logo, stages

kata_hewan = ["banteng", "cendrawasih", "domba", "harimau", "kangguru"]

kata_terpilih = random.choice(kata_hewan)
sisa_nyawa = 6

hasil_tebakan_user = []
for n in range(len(kata_terpilih)):
  hasil_tebakan_user.append("_")

print(logo)
print("Tema Kata adalah Hewan")

while "_" in hasil_tebakan_user:
  tebakan_user = input("Tebak sebuah huruf: ").lower()
  
  if tebakan_user in hasil_tebakan_user:
    print(f"Kamu sudah menebak {tebakan_user}")

  for posisi in range(len(kata_terpilih)):
    huruf = kata_terpilih[posisi]
    if tebakan_user == huruf:
      hasil_tebakan_user[posisi] = huruf

  if tebakan_user not in kata_terpilih:
    print(f"Anda menebak {tebakan_user}, itu tidak ada dalam kata. Anda kehilangan 1 nyawa.")
    sisa_nyawa -= 1
    if sisa_nyawa == 0:
      print("Kamu kalah")
      break
  
  print(f"{' '.join(hasil_tebakan_user)}")
  print(stages[sisa_nyawa])
else:
  print("Kamu menang!")

print(stages[sisa_nyawa])