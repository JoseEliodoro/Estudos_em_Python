import json
#Exercício 10.11
filename = 'capitulo10/favorite_number.json'
""" 
favorite_number = input("Digite seu número favorito: ")
with open(filename, 'w') as f_obj:
    json.dump(favorite_number, f_obj)
    
with open(filename) as f_obj:
    favorite_number = json.load(f_obj)
    
print('Eu sei qual seu número favorito! É '+ favorite_number) 
"""

#Exercício 10.12
def msg_number():
    favorite_number = get_number()
    if(favorite_number):  
        print('Eu sei qual seu número favorito! É '+ favorite_number)
    else:
        get_new_number()
        
    
def get_new_number():
    with open(filename, 'w') as f_obj:
        favorite_number = input('Digite seu número favorito: ')
        json.dump(favorite_number, f_obj)  
        
        
def get_number():
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


msg_number()
