import json
""" 
filename = 'arquivos/username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
        
except FileNotFoundError:
    username = input('What is your name? ')

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("we'll remember you when you come back, %s!"%username)

else:
        print('Welcome back, %s!'%username) 
"""

#Refatoração do código acima
def get_stored_user(): #Obtém o nome do usuário já armazenado se estiver disponível.
    filename = 'arquivos/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            
    except FileNotFoundError:
        return None
    else: 
        return username
        
        
def greet_user(): #Saúda o usuário pelo nome.
    username = get_stored_user()
    if(username):
        print('Welcome back, %s!'%username) 
    else:
        username = get_new_username()
        print("we'll remember you when you come back, %s!"%username) 


def get_new_username(): #Pede um novo nome de usuário.
    filename = 'arquivos/username.json'
    username = input('What is your name? ')

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


greet_user()