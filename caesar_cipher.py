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
        print(f"\nEncrypted Text: {encrypted_text}")
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
        print(f"\nDecrypted Text: {decrypted_text}")

print("WELCOME TO CAESAR CIPHER PROGRAM!")

user_continue = True

while user_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    caesar_chiper(text, shift, direction)

    yes_or_no = input("\nType 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if yes_or_no == 'no':
        user_continue = False
        print("\nGoodbye!")
