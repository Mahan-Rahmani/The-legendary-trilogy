import random
import string
chars = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
all = chars + numbers + symbols
while True:
    print('Choose an option:\n\t1)Create password\n\t2)Exit')
    choice = input('your choice:')
    if choice == '1':
        lenght = int(input('length of password:'))
        password = ''.join(random.sample(all, lenght))
        print(password)
    elif choice == '2':
        print('goooodbyeeee!!!')
        break
    else:
        print('wrong choice')
