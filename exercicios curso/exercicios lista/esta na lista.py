numbers = [5, 6, 7, 9, 2, 1, 4, 3, 8, 0]

number = int(input('DIGITE UM NÚMERO: '))

if number in numbers:
    print('O NÚMERO %d ESTÁ NA LISTA %s'%(number, numbers))
else:
    print('O NÚMERO %d NÃO ESTÁ NA LISTA %s'%(number, numbers))
d = 'pizza'
if d in 'z':
    print('foi')