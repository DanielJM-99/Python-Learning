from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_decode):
    output_text = ""

    if encode_decode == "decode":
            shift_amount *= -1  # Reverse the shift when decoding

    for letter in original_text:
        if letter in alphabet:
            shifted_letter = alphabet.index(letter) + shift_amount
            shifted_letter %= len(alphabet)  # Ensure wrap-around
            output_text += alphabet[shifted_letter]
        else:
            output_text += letter
    
    print(f"Here is the {encode_decode}d text: {output_text}")

keep_ceaser = True
while keep_ceaser:

    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift =  int(input("Type the shift number: \n"))
    ceaser(original_text=text, shift_amount=shift, encode_decode=direction)

    keep_playing = input("Do you want to keep encoding/decoding? 'Yes' or 'No'\n").lower()
    
    if keep_playing == "no":
        keep_ceaser = False
        print("Byeee")
    