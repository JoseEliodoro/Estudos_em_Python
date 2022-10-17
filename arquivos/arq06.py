import json #Biblioteca para trabalhar com json

numbers = [2, 3, 5, 7, 11, 13]
filename= 'arquivos/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
    #Comando que armazena em formato de json

with open(filename) as f_obj:
    numbers2 = json.load(f_obj)
print(numbers2)

#Lembrando do nome do usuário
filename = 'arquivos/username.json'
""" 
username = input('What is your name? ')

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
print("we'll remember you when you come back, %s!"%username)
"""
with open(filename) as f_obj:
    username = json.load(f_obj)
    print('Welcome back, %s!'%username)
