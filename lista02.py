lista = [7, 5, 1, 3, 9, 2]
lista_animal = ['gato', 'cachorro', 'elefante', 'peixe']

#Ordena lista de forma crescente
print('lista = {}' 
      '\nlista_animal = {}'
      .format(lista, lista_animal))

print(sorted(lista)) #A função sorted() recebe uma lista e devolve ela ordenada, de forma temporária 

lista.sort() #O método .sort() ordena uma lista permanentemente
lista_animal.sort()

print('lista = {}'
      '\nlista_animal = {}'
      .format(lista, lista_animal))

#lista.sort(reverse = True) #Ordena de forma invertida da forma como ela está
lista.reverse() 
print(lista)

print(len(lista_animal)) #A função len() retorna a quantidade de elementos da lista