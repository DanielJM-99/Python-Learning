# Caesar Cipher part 2

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Todo 1 
def encrypt(original_text, shift_amount):
    # Todo 2
    enconded_word = ""
    for letter in original_text:
        # Get index of letter and store it
        shifted_letter = alphabet.index(letter) + shift_amount
        # Add new letter to encoded word
        shifted_letter %= len(alphabet)
        enconded_word += alphabet[shifted_letter]
    print(enconded_word)

def decrypt(original_text, shift_amount):
    # Todo 2
    decoded_word = ""
    for letter in original_text:
        # Get index of letter and store it
        shifted_letter = alphabet.index(letter) - shift_amount
        # Add new letter to encoded word
        shifted_letter %= len(alphabet)
        decoded_word += alphabet[shifted_letter]
    print(decoded_word)

def ceaser(election, to_cypher, number_shift):
    if election == "encode":
        encrypt(to_cypher, number_shift)
    else:
        decrypt(to_cypher, number_shift)

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower().lower()
shift = int(input("Type the shift number: \n"))

ceaser(election=direction, to_cypher=text, number_shift=shift)
