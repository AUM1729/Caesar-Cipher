def caesar_cipher_encrypt(text, shift):
    result = ""

    # Traverse through the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Keep spaces and non-alphabetical characters the same
        else:
            result += char

    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    while True:
        # Display options to the user
        print("\nSelect an option:")
        print("1: Encrypt")
        print("2: Decrypt")
        print("0: Exit")
        
        # Get user input for option
        option = input("Enter your choice (1/2/0): ")

        if option == '1':
            # Encrypt option
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif option == '2':
            # Decrypt option
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        elif option == '0':
            # Exit option
            print("Exiting the program.")
            break

        else:
            # Invalid input handling
            print("Invalid choice! Please choose 1, 2, or 0.")

if __name__ == "__main__":
    main()
