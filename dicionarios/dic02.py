favorite_languages ={
    'jose': 'javascript',
    'carlos': 'python',
    'eliodoro': 'java',
    'santana': 'c#',
    'gildo': 'portugol',
    'eliodorio': 'assembly'
}
#Percorre um dicionário com o primeiro valor sendo a chave e o segundo sendo o valor
for key, value in favorite_languages.items():
#O método .items() retorna uma lista contendo cada par chave-valor dentro de uma tupla
    print('chave: '+ key +'    valor: '+ value)
    
#Percorrendo as chaves do dicionário
for key in favorite_languages.keys():
#O método .keys() retorna uma lista contendo cada chave que está no dicionário
    print(key)
    
#Percorrendo os valores do dicionário
for value in favorite_languages.values():
#O método .values() retorna uma lista contendo cada valor que está no dicionário
    print(value)