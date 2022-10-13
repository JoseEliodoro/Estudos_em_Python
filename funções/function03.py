#Use asteriscos para fazer n-argumentos
def make_pizza(*topping): #Esse asterisco retorna uma tupla com os argumentos que foram passados
    print(topping)
    
""" make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese') """


def build_profile(first, last, **user_info):
    """ 
    Ao colocar nessa estrutura a cima ele vai criar um dicionário contendo os valores que 
    foram  passados como argumento, adicionando os argumentos nomeados que foram passados que 
    não possuem uma variável para si 
    """
    profile = {}
    profile['first_name'] = first 
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

""" user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile) """