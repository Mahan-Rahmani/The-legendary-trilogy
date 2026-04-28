def encrypt(text, multiplier=6, offset=12):
    encrypt_text = ""
    for char in text:
        encrypt_text += chr(ord(char) * multiplier + offset)
    return encrypt_text

def decrypt(text, multiplier=6, offset=12):
    decrypt_text = ""
    for char in text:
        decrypt_text += chr((ord(char) - offset) // multiplier)
    return decrypt_text

def menu():
    print('What do you want?\n\t1) Encrypt\n\t2) Decrypt\n\t3) Quit')

def main():
    while True:
        menu()
        choice = input('Your choice: ')
        
        if choice == '1':
            plain_text = input('Enter your Encryption Key: ')
            print('Encrypted text:', encrypt(plain_text))
        
        elif choice == '2':
            cipher_text = input('Enter your Decryption Key: ')
            print('Decrypted text:', decrypt(cipher_text))
        
        elif choice == '3':
            print('Goodbye!')
            break
        
        else:
            print('Invalid choice!\n')
        print('*' * 50 + '\n')

if __name__ == "__main__":
    main()
