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

players = ['charles', 'martina', 'michael', 'florence', 'eli']
player = players[0:5] #Fatia de uma lista no primeiro elemento coloque o inicio e no segundo o final
'''
Caso o primeiro elemento seja omitido inicio é definido como 0
Caso o segundo seja elemento seja omitido final é definido como último elemento da lista
Caso o terceiro elemento seja omitido o passo é definido como 1
Caso o primeiro elemento seja negativo ele apresenta os últimos colocados da lista
'''
print(player)

foods = ['pizza', 'feijoada', 'pastel', 'coxinha']
food = foods[:] #Copia uma lista
'''
Quando colocamos food = foods, as listas ficam conectadas se mudarmos o valor de foods muda o valor de food, para copiar o valor sem fazer referencia a outra lista usamos esse método
'''
print(food)