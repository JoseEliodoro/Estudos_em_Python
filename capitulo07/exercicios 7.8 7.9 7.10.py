import os

#Exercício 7.8, 7.9
sandwich_orders = ['pastrami', 'sanduíche de atum', 'pastrami', 'sanduíche frango', 'sanduíche de queijo', 'pastrami']
finished_sandwiches = []
print('A lanchonet esta sem pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    sandwiche = sandwich_orders.pop()
    print('Preparei seu '+ sandwiche)
    finished_sandwiches.append(sandwiche)

print('\n-----Sanduíches prontos-----')
for sandwiche in finished_sandwiches:
    print(sandwiche)
    

os.system('cls')

#Exercício 7.10
prompt = 'Se pudesse visitar um lugar do mundo, para onde você iria? '
favorite_place = dict()
active = True
while active:
    os.system('cls')
    user_name = input('Informe seu nome de usuário: ')
    if(user_name in favorite_place.keys()):
        print("Usuário já preencheu o formulario")
        os.system('pause')
        continue
    user_place = input(prompt)
    favorite_place[user_name] = user_place
    r = input('Continuar com novo usuário? (yes/no) ')
    if(r == 'no'):
        active = False
    
for user, place in favorite_place.items():
    print('O usuário %s deseja ir para %s'%(user, place))