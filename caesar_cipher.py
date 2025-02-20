from art import logo

print(logo)

def caesar_chiper(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        encrypted_text = ""
        for i in range(len(original_text)):
            char = original_text[i]
            if char.islower():
                encrypted_text += chr((ord(char) + shift_amount - 97) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                encrypted_text += char
        print(f"Encrypted Text: {encrypted_text}")
    else:
        decrypted_text = ""
        for i in range(len(original_text)):
            char = original_text[i]
            if char.islower():
                decrypted_text += chr((ord(char) - shift_amount - 97) % 26 + 97)
            elif char.isupper():
                decrypted_text += chr((ord(char) - shift_amount - 65) % 26 + 65)
            else:
                decrypted_text += char
        print(f"Decrypted Text: {decrypted_text}")

user_continue = True

while user_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar_chiper(text, shift, direction)

    yes_or_no = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if yes_or_no == 'no':
        user_continue = False
        print("Goodbye")
