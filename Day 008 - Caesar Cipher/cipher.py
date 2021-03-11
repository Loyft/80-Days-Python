from alphabet import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def cipher(direction, text, shift):
    shift = shift % 26
    new_text = ''
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_text += alphabet[position + shift]
            elif direction == 'decode':
                new_text += alphabet[position - shift]
        else:
            new_text += char
    print(f"the {direction}d text is: {new_text}")

cipher(direction, text, shift)
