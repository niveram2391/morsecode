MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def encrypt(word):
    # encrypted_key = [MORSE_CODE_DICT[letter] for letter in word]
    # print(f"Morse code of {word} is {encrypted_key}")
    morse_code = ''
    for letter in word:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT[letter] + ' '
        else:
            morse_code += '  '

    return morse_code
def decrypt(code):
    translate = ''
    for value in code.split(' '):
        for key,values in MORSE_CODE_DICT.items():
            if value == values:
                translate += key
            elif value == ' ':
                translate += value

    return translate


choice = input(" Do you want to encrypt/decrypt : ").lower()
if choice == 'encrypt':
    word = input("Please enter a word to convert to morse code : ")
    encrypted_key = encrypt(word)
    print(f"Morse code of {word} is {encrypted_key}")
elif choice == 'decrypt':
    code = input(" Please enter morse code :")
    decrypted_word = decrypt(code)
    print(f" {code} is {decrypted_word}")
else :
    print("Incorrect Choice")
