#Exercício 4.10
persons = ['jose', 'carlos', 'eliodoro', 'santana']

print('os três primeiros itens da lista são: %s' %(persons[:3]))
print('Os três últimos itens da lista são: %s' %(persons[-3:]))

#Exercício 4.11
pizzas = ['calabresa', 'mussarela', 'frango com catupiry']
friend_pizzas = pizzas[:]

pizzas.append('Quatro queijos')
friend_pizzas.append('Portuguesa')

print('Minhas pizzas favoritas são:', pizzas)
print('As pizzas favoritas de meu amigo são:', friend_pizzas)

#Exercício 4.12
foods = ['pizza', 'feijoada', 'pastel', 'coxinha']
for food in foods:
    print(food)

