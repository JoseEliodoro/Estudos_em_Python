#Exercício 5.8
users = ['jose', 'madara', 'midoria', 'admin']
users.sort()

for user in users:
    if(user.lower() == 'admin'):
        print(f"Olá {user}, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {user}, obrigado por fazer login novamente.")
        
#Exercício 5.9
cont = len(users)
while(cont > 0):
    del(users[cont - 1])
    cont -= 1


if(not(users)):
    print('Precisamos encontrar alguns usuários!')
            
#Exercício 5.10
current_users = ['joSe', 'madara', 'midoria', 'maki', 'gojo']
new_users = ['carlos', 'josE', 'ciro', 'gildo', 'maki']

new = list()
for user in current_users:
    new.append(user.lower())
    
for user in new_users:
    if(user.lower() in new):
        print(f"O nome de usuário '{user}' já está em uso, informe outro")
    else:
        print(f"O usuário '{user}' está disponível")
                    
#Exercício 5.11
numbers = list(range(1,10))
for number in numbers:
    if(number == 1):
        print('%dst'%(number))
    elif(number == 2):
        print('%dnd'%(number))
    elif(number == 3):
        print('%drd'%number)
    else:
        print('%dth'%number)