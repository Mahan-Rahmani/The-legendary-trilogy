import time
while True:
    choice = input('Do you want to start the timer? (y/n): ')
    if 'y' in choice.lower():
        hours = int(input('How many hours do you want to start?: '))
        minutes = int(input('How many minutes do you want to start?: '))
        seconds = int(input('How many seconds do you want to start?: '))
        total = hours * 60 * 60 + minutes * 60 + seconds
        print('The timer is starting...')
        time.sleep(1)
        while total > 0:
            print(total)
            total -= 1
            time.sleep(1)
    elif 'n' in choice.lower():
        print('Goodbye')
        break
    else:
        print('invalid input...')
