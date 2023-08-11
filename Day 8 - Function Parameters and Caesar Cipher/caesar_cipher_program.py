from caesar_cipher_art import logo

# Import and display the logo from caesar_cipher_art.py when the program is first run.
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Combine the encryption() and decryption() functions into one function called caesar_cipher().
# Parameters are taken from 'text', 'shift', and 'choice'.
def caesar_cipher(input_text, input_shift, input_choice):
    result = ""
    if input_choice == "decrypt":
        input_shift *= -1
        
    for letter in input_text:
        if letter in alphabet:
            # If the user enters 'shift' greater than many letters in 'alphabet', 
            # then get the quotient between the sum of the letter index and shift by 26.
            new_letter = (alphabet.index(letter) + input_shift) % 26
            result += alphabet[new_letter]
        else:
            # If the user types a number/symbol/space, then write it back unchanged.
            result += letter

    # Display the encryption or decryption result.
    print(f"Result {input_choice}: {result}")

# The program will continue to run until the user types "no"
end_program = False

while not end_program:
    choice = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    text = input("Type message:\n").lower()
    shift = int(input("Type the desired shift:\n"))
    caesar_cipher(input_text=text, input_shift=shift, input_choice=choice)
    
    # If the user types 'no', the program will stop.
    if input("Type 'yes' if you want to repeat the program or type 'no' if you want to finish.\n") == "no":
        end_program = True
        print("Bye!")