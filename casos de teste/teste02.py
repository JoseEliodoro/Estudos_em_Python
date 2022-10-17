from teste01 import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input('\nPlease give me a first name: ')
    if(first == 'q'):
        break
    last = input('Please give me a lasta name: ')
    if(last == 'q'):
        break
    print('\tNeatly formatted name:', get_formatted_name(first, last))