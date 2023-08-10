from caesar_cipher_art import logo

# Impor dan tampilkan logo dari caesar_cipher_art.py ketika program pertama kali dijalankan.
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Kombinasikan fungsi enkripsi() dan dekripsi() ke dalam satu fungsi bernama caesar_cipher().
# Parameter diambil dari 'text', 'shift', dan 'choice'.
def caesar_cipher(input_text, input_shift, input_choice):
    hasil = ""
    if input_choice == "dekripsi":
        input_shift *= -1
        
    for huruf in input_text:
        if huruf in alphabet:
            # Jika user memasukkan 'shift' lebih besar dari banyak huruf di 'alphabet', 
            # maka dapatkan hasil sisa bagi antara penjumlahan index huruf dan shift dengan 26.
            huruf_baru = (alphabet.index(huruf) + input_shift) % 26
            hasil += alphabet[huruf_baru]
        else:
            # Jika user mengetikkan nomor/simbol/spasi, maka tulis kembali tanpa diubah.
            hasil += huruf

    # Tampilkan hasil enkripsi atau dekripsi.
    print(f"Hasil {input_choice}: {hasil}")

# Program akan terus jalan hingga user mengetikkan "tidak"
akhir_program = False

while not akhir_program:
    choice = input("Ketik 'enkripsi' untuk enkripsi, ketik 'dekripsi' untuk dekripsi:\n")
    text = input("Ketik pesan:\n").lower()
    shift = int(input("Ketik pergeseran yang diinginkan:\n"))
    caesar_cipher(input_text=text, input_shift=shift, input_choice=choice)
    
    # Jika user mengetikkan 'tidak', maka program akan berhenti.
    if input("Ketik 'ya' jika ingin ulang program atau ketik 'tidak' jika ingin selesai.\n") == "tidak":
        akhir_program = True
        print("Sampai jumpa!")