import os
from sqlite3 import apilevel
questions = [
    {
        'tema': 'comidas',
        'palavras': [
            'Arroz', 'pizza', 'feijoada', 'sorvete',
            'cuscuz', 'arroz doce', 'lasanha', 'dobradinha',
            'macarronada'
        ]
    },
    {
        'tema': 'pais',
        'palavras': [
            'brasil', 'estados unidos', 'venezuela', 'rússia',
            'canadá', 'alemanha', 'inglaterra', 'madacáscar',
            'japão', 
        ]    
    },
]

i = 0
#Escreve as opções de tema
while(i < len(questions)):
    print('Digite %d para %s'%(i, questions[i]['tema']),)
    i += 1
#Recebe o tema escolhido
topic = int(input('DIGITE UM NÚMERO: '))
word = int(input('DIGITE UM NÚMERO DE 0 à %d: ' %(len(questions[topic]['palavras']) - 1)))

os.system('cls')
w = questions[topic]['palavras'][word] #Palavra a ser jogada
word = [letter for letter in w] #Palavra na lista
p = ['_' for x in range(0, len(word))] #Lista que vai ser mostrada
b = p[:] #copia da lista

life = 5 #vidas
alphabet = list() #Criação de alfabeto

while(word != b):
    tema = questions[topic]['tema']
    os.system('cls')
    print(f'TEMA: {tema}')
    print(f'VIDA: {life}') #Controle de vida
    print(f'ALFABETO: {alphabet}')
    print(p)
    
    if(life > 0):
        letter = input('DIGITE UMA LETRA: ') #Recebe uma letra digitada pelo usuário
        if(letter.upper() in alphabet):
            print('LETRA JÁ INFORMADA')
            os.system('pause')
        else:
            alphabet.append(letter.upper())
            alphabet.sort()
            if(letter.lower() in word):
                i = 0
                while(i < len(word)):
                    if(word[i] == letter):
                        word[i] = '_' #Remove da lista feita com a palavra
                        p[i] = letter.upper() #Coloca na lista de resposta
                    i += 1
            else:
                life -= 1
    else:
        
        print('GAME OVER!!!')
        print('A PALAVRA ERA %s'%(w.upper()))
        break
    
if(life > 0):
    print('PARABÉNS VOCÊ GANHOU!!!')
    
os.system('pause')