while True:
    print('what do you want?\n\t1)Encrypt\n\t2)Decrypt\n\t3)Quit')
    choice = input('your choice: ')
    if choice == '1':
        plain_text = input('enter your Encryption Key:')
        Encrypt_text = ""
        for p in plain_text:
            x = ord(p) * 6 + 12
            Encrypt_text += chr(x)
        print('Encrypt_text:',Encrypt_text)
        print('*' * 50 + '\n')
    elif choice == '2':
        plain_text = input('enter your Decryption Key: ')
        Decrypt_text = ""
        for d in plain_text:
            y = (ord(d) - 12) // 6
            Decrypt_text += chr(y)
        print('Decrypt_text: ',Decrypt_text)
        print('*' * 50 + '\n')
    elif choice == '3':
        print('goodbye!!!')
        break
    else:
        print('invalid choice')
