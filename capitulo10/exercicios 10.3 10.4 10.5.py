#Exercício 10.3
""" 
filename = 'capitulo10\guest.txt'

with open(filename, 'a') as file_object:
    
    name = input('Digite seu nome: ')
    file_object.write(name+'\n')    
"""

#Exercício 10.4
""" filename = 'capitulo10\guest_book.txt'

with open(filename, 'a') as file:
    
    list_name = []
    x = ''
    while x != 'n':
        list_name.append(input('Digite seu nome: '))
        x = input('Você deseja adicionar mais alguém? [S/N] ')
    
    print('Sejam bem vindos!!!')
    for person in list_name:
        file.write(person+'\n') """
        
#Exercício 10.5
import os
def add(option):
    with open('capitulo10\enquete.txt', 'r') as file_object:
        lines = file_object.readlines()
        
        cont = 1
        while cont <= 6:
            if(cont-1 == int(option)-1):
                lines[cont-1] = int(lines[cont-1]) + 1
            else:
                lines[cont-1] = lines[cont-1].strip()
            cont += 1
        write(lines)
        
def write(lines):
    with open('capitulo10\enquete.txt', 'w') as file_object:
        file_object.write('')
            
    with open('capitulo10\enquete.txt', 'a') as file_object:
        for line in lines:
            file_object.write('%s\n'%line)
            

            
list_options = ['1', '2', '3', '4', '5', '6']
option = None
while not(option in list_options):
    os.system('cls')
    print('Qual linguagem você prefere?'
          '\n1-para Pythonn   2-para C'
          '\n3-para C#        4-para PHP'
          '\n5-para Java      6-para JavaScript')
    option = input('Escolha uma das opções acima: ')
add(option)
    