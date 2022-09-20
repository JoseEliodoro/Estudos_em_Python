lista = [7, 5, 1, 3, 9, 2]
lista_animal = ['gato', 'cachorro', 'elefante', 'peixe']
lista_mista = [2, 'gato', True, .5, 'arroz']
#print(lista_mista) #imprime a lista
#nova_lista = lista * 3 #repede os valores da lista

#lista os elementos da lista
'''
for x in lista_animal:
    print(x)


#print(sum(lista)) #soma os elementos de uma lista de inteiros
#print(max(lista)) #maior valor da lista funciona para string
#print(min(lista)) #menor valor da lista funciona para string

#Verifica se existe um elemento na lista
if 'lobo' in lista_animal:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista')
    lista_animal.append('lobo') #add na lista como último elemento

print(lista_animal)
lista_animal.pop() #Remove o último elemento da lista, posso informar a posição dentro dos parenteses

lista_animal.remove('gato') #Remove um elemento da lista pelo valor
print(lista_animal)
'''
'''
#Ordena lista de forma crescente
print('lista = {}' 
      '\nlista_animal = {}'
      .format(lista, lista_animal))

lista.sort()
lista_animal.sort()
print('lista = {}'
      '\nlista_animal = {}'
      .format(lista, lista_animal))
lista.reverse() #Ordena de forma reversa
'''