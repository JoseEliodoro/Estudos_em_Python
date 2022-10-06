#Exercício 6.4
glossario = {
    'tupla': 'Um n-ordenado o qual não pode mudar seus valores',
    'objeto': 'Uma instância de uma classe',
    'laço': 'Uma estrutura que repete até que seu resultado lógico seja falso',
    'condicional': 'Estrutura que imponhe uma condição',
    'range': 'Um tipo de lista diferenciado o qual faz uma lista de numeros com o primeiro argumento sendo seu início,o segundo sendo seu final e último sendo seu passo '
}
for key, value in glossario.items():
    print(key+':\n'+value)

#Exercício 6.5
rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'amstel': 'holanda'
}
for k, v in rios.items():
    print(f"O rio {k} corre pelo {v}")
    
for k in rios.keys():
    print(k)
    
for v in rios.values():
    print(v)
    
#Exercício 6.6
favorite_languages ={
    'jose': 'javascript',
    'carlos': 'python',
    'eliodoro': 'java',
    'santana': 'c#',
    'gildo': 'portugol',
    'eliodorio': 'assembly'
}
new_persons = ['jose', 'madara', 'carlos', 'kira', 'edward']

for person in new_persons:
    if person in favorite_languages.keys():
        print(f"Sr(a) {person} obrigado por responder a pergunta")
    else:
        print(f"Sr(a) {person} você ainda não respondeu a pesquisa")