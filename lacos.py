from http.client import responses
import os

prompt = '\nPlease enter the name os a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished.) "

while False: #Executa o laço eternamente
    os.system('cls')
    city = input(prompt)
    if(city.lower() == 'quit'):
        break
    else:
        print("I'd love to go to %s!"%(city.title()))
    os.system('pause')

current_number = 11
while current_number < 10:
    current_number += 1
    if(current_number % 2 == 0):
        continue #Faz o laço recomeçar sem necessariamente chegar no fim dele
    print(current_number)
    

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = ['admin', 'srnz']

while unconfirmed_users: #Utilizar o laço while assim repete a quantidade de elementos da lista
    current_user = unconfirmed_users.pop()
    print('Verifying user: '+current_user.title())
    confirmed_users.append(current_user)
    
print('\nThe following users have been confirmed: ')
for user in confirmed_users:
    print(user.title())
    
#Removendo todos os valores iguais numa lista
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

os.system('cls')

responses = {} #cria dicionário vazío 
polling_active = True #Criação de variável flag
while polling_active:
    name = input('What is your name? ')
    response = input('Which mountain would you like to climb someday? ')
    responses[name] = response #Insere o nome da pessoa como chave e a montanha como valor
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if(repeat == 'no'):
        polling_active = False #Saida do faço através do flag
        
#Mostrando os resultados contidos no dicionário
print('\n---Poll Results---')
for name, response in responses.items():
    print(name +' would like to climb '+ response +'.')