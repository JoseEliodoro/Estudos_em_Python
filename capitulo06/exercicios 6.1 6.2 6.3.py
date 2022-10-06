#Exercício 6.1
person = {
    'first_name': 'josé carlos',
    'last_name': 'eliodoro',
    'age': 19,
    'city': 'igarassu'
}
for data in person:
    print(data, ':',person[data])
    
#Exercício 6.2
favorite_number = {
    'jose': 5,
    'kira': 30,
    'madara': 6,
    'carlos': 31,
    'gildo': 30
}
for key in favorite_number:
    print('O numero favorido de %s é %d'%(key, favorite_number[key]))

#Exercício 6.3
glossario = {
    'tupla': 'Um n-ordenado o qual não pode mudar seus valores',
    'objeto': 'Uma instância de uma classe',
    'laço': 'Uma estrutura que repete até que seu resultado lógico seja falso',
    'condicional': 'Estrutura que imponhe uma condição',
    'range': 'Um tipo de lista diferenciado o qual faz uma lista de numeros com o primeiro argumento sendo seu início,o segundo sendo seu final e último sendo seu passo '
}
for key, value in glossario.items():
    print(key+':\n'+value)
print(glossario.items())