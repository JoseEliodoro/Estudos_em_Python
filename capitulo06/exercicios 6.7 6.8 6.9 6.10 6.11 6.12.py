#Exercício 6.7
person01 = {
    'first_name': 'josé carlos',
    'last_name': 'eliodoro',
    'age': 19,
    'city': 'igarassu'
}
person02 = {
    'first_name': 'gildo',
    'last_name': 'Eliodorio',
    'age': 47,
    'city': 'igarassu'
}
person03 = {
    'first_name': 'madara',
    'last_name': 'uchira',
    'age': 'died',
    'city': 'konoha'
}
people = [person01, person02, person03]

for person in people:
    print(f"\nFull name: {person['first_name']}" 
          f" {person['last_name']}"
          f"\nAge: {person['age']}"
          f"\nCity: {person['city']}")

#Exercício 6.8
corvo = {
    'tipo': 'corvo',
    'dono': 'itachi'
}
basilisco = {
    'tipo': 'basilisco',
    'dono': 'voldemort'
}
mahoraga = {
    'tipo': 'mahoraga',
    'dono': 'megumi'
}
pets = [corvo, basilisco, mahoraga]
for pet in pets:
    print(f"\ntipo: {pet['tipo']}" 
          f"\nDono: {pet['dono']}")
    
#Exercício 6.9
favorite_place = {
    'jose': 'canada',
    'carlos': 'japão',
    'eliodoro': 'reino unido'
}
for person, place in favorite_place.items():
    print('O lugar favorito de %s é %s\n'%(person, place))
    
    
#Exercício 6.10
favorite_number = {
    'jose': [5, 8 , 9],
    'kira': [30, 7, 6,],
    'madara': [6, 45, 34,],
    'carlos': [31, 52, 54,],
    'gildo': [30, 78, 34,]
}
for name, listNumber in favorite_number.items():
    print('Os numeros favorido de %s são %s'%(name, listNumber))

#Exercício 6.11
cities = {
    'igarassu': {
        'country': 'brasil',
        'population': 109.332,
        'fact': 'eu moro aqui'
    },
    'kyoto': {
        'country': 'japão',
        'population': 1475000,
        'fact': 'eu quero visitar'
    },
    'vancouver': {
        'country': 'canada',
        'population': 2463431,
        'fact': 'chove demais'
    }
}

for city, city_info in cities.items():
    print('A cidade de %s, que fica no %s'%(city, city_info['country']),
          'tem uma população de %s'%(city_info['population']),
          'um fato interessante é que %s'%(city_info['fact']))