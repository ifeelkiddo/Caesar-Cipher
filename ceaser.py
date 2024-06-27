import time
def caesar_cipher_encrypt(text, shift):
    encrypted_message = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Encryption Decryption Program")
    time.sleep(2)
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                encrypted_message = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted message: {encrypted_message}")
            else:
                decrypted_message = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")

        continue_choice = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()