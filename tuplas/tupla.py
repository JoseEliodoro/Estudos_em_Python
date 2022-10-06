#Tuplas são imutáveis 
tupla = (10, 14, 1, 12)
lista_mamiferos = ['elefante', 'vaca', 'leão', 'humano']

print(len(tupla)) #Diz a quantidade de elementos
lista_mamiferos = tuple(lista_mamiferos)
print(type(lista_mamiferos))
tupla = list(tupla)
tupla.sort()
print(tupla)