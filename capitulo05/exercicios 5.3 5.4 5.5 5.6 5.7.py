import os
#Exercício 5.3
alien_color = 'green'
if(alien_color == 'green'):
    print('jogador acabou de ganhar 5 pontos.')
    
alien_color = 'red'
if(alien_color == 'green'):
    print('jogador acabou de ganhar 5 pontos.')

#Exercício 5.4
if(alien_color == 'green'):
    print('jogador acabou de ganhar 5 pontos.')
else:
    print('jogador acabou de ganhar 10 pontos.')
    
#Exercício 5.5
if(alien_color == 'green'):
    print('jogador acabou de ganhar 5 pontos.')
elif(alien_color == 'yellow'):
    print('jogador acabou de ganhar 10 pontos.')
else:
    print('jogador acabou de ganhar 15 pontos.')
 
#Exercício 5.6
#os.system('pause')
os.system('cls')

age = 15 #int(input('Digite sua idade: '))
if(age < 2):
    print("Você é um bebê")
elif(age >= 2 and age < 4):
    print("Você é uma criança")
elif(age >= 4 and age < 13):
    print("Você é um(a) goroto(a)")
elif(age >= 13 and age < 20):
    print('Você é um(a) adolescente')
elif(age >= 20 and age < 65):
    print('Você é um adulto')
else:
    print('Você é um idoso')
    
#Exercício 5.7
favorite_fruits = ['banana', 'laranja', 'uva']
if(favorite_fruits in 'banana'):
    print('Você realmente gosta de banana')
if(favorite_fruits in 'uva'):
    print('Você realmente gosta de uva')
if(favorite_fruits in 'maçã'):
    print('Você realmente gosta de maçã')
if(favorite_fruits in 'tomate'):
    print('Você realmente gosta de tomate')
if(favorite_fruits in 'laranja'):
    print('Você realmente gosta de laranja')