import os

#Exercício 7.4
ingrediente = 'quit'
while ingrediente.lower() != 'quit':
    ingrediente = input('Digite um ingrediente para a pizza: ')
    if(ingrediente != 'quit'):
        print(ingrediente +' foi adicionado na pizza!')
        
#Exercício 7.5
age = -1
while age != -1:
    os.system('cls')
    age = int(input("Caso queira sair digite '-1'"
        "\nInforme sua idade: "))
    if(age >= 0 and age < 3):
        print('O ingresso gratuito.')
    elif(age >= 3 and age < 12):
        print('O ingresso custa 10 dólares.')
    elif(age >= 12):
        print('O ingresso custa 15 dólares')
    os.system('pause')
    
     
#Exercício 7.6
active = True
while active:
    ingrediente = input('Digite um ingrediente para a pizza: ')
    if(ingrediente != 'quit'):
        print(ingrediente +' foi adicionado na pizza!')
    else:
        active = False
        
#Exercício 7.7
""" cont = 1
while True:
    print(cont)
    cont += 1 """