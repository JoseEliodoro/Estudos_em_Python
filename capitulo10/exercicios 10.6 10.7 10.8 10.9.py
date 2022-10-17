#Exercício 10.6
def sum(a, b):
    soma = a + b
    print('%d + %d = %d'%(a, b, soma))
    
""" 
try:
    x = int(input('Digite o primeiro número para a soma: '))
    y = int(input('Digite o segundo número para a soma: '))
except ValueError:
    print('O que você digitou não é um número inteiro')
else:
    sum(x, y) 
"""
    
#Exercício 10.7
import os
while False:
    os.system('cls')
    print("Coloque 'q' caso queira sair")
    x = input('Digite o primeiro número para a soma: ')
    if(x == 'q'): break
    y = 5#input('Digite o segundo número para a soma: ')
    if(y == 'q'): break
    try:
        x, y = int(x), int(y)
    except ValueError:
        print('O que você digitou não é um número inteiro')
    else:
        sum(x, y)
    os.system('pause')
    
    
#Exercício 10.8
def name(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.readlines()
    except FileNotFoundError:
        print('\narquivo {} não encontrato'.format(filename))
    else:
        title = filename.replace('.txt', '').replace('capitulo10/', '')
        print('\n'+title.upper())
        for name in contents:
            print(name.strip().title())
            
filenames = ['cats.txt', 'fish.txt', 'dogs.txt']
for file in filenames:
    name('capitulo10/'+file)


#Exercício 10.9
def name2(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
    else:
        title = filename.replace('.txt', '').replace('capitulo10/', '')
        print('\n'+title.upper())
        for name in contents:
            print(name.strip().title())
            

for file in filenames:
    name2('capitulo10/'+file)


