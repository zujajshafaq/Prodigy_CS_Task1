def caesar_cipher_enp(text, shift):
    enp_txt = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            enp_txt += chr(shifted)
        else:
            enp_txt += char
    return enp_txt

def caesar_cipher_dep(text, shift):
    return caesar_cipher_enp(text, -shift)

def main():
    print("Caesar Cipher encryption/decryption")
    while True:
        choice = input("Do you want to encrypt (E) or decrypt (D) a text? ").upper()
        
        if choice == 'E':
            msg = input("Enter the text to encrypt: ")
            shift = int(input("Shift value (integer): "))
            enp_msg = caesar_cipher_enp(msg, shift)
            print(f"Encrypted text: {enp_msg}")
        elif choice == 'D':
            msg = input("Enter the text to decrypt: ")
            shift = int(input("Shift value (integer): "))
            dep_msg = caesar_cipher_dep(msg, shift)
            print(f"Decrypted text: {dep_msg}")
        else:
            print("Invalid choice.")
            continue
        
        exit_choice = input("Do you want to exit the program? (yes/no): ").lower()
        if exit_choice == 'yes':
            print(" program Exit.")
            break
        elif exit_choice == 'no':
            continue
        else:
            print("Invalid choice, restarting the program.")
            continue

if __name__ == "__main__":
    main()
