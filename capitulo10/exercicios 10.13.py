import json

def get_stored_user(): #Obtém o nome do usuário já armazenado se estiver disponível.
    filename = 'capitulo10/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            
    except FileNotFoundError:
        return None
    else: 
        username = verify_username(username)
        return username
        
        
def verify_username(username):
    verify = input('Seu nome é {}? [S/N] '.format(username))
    if(verify == 'N' or verify == 'n'):
        return  None
    return username
        
def greet_user(): #Saúda o usuário pelo nome.
    username = get_stored_user()
    if(username):
        print('Welcome back, %s!'%username) 
    else:
        username = get_new_username()
        print("we'll remember you when you come back, %s!"%username) 


def get_new_username(): #Pede um novo nome de usuário.
    filename = 'capitulo10/username.json'
    username = input('What is your name? ')

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


greet_user()