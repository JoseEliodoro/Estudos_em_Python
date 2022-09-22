magicians = ['alice', 'david', 'carolina']

for magician in magicians: #For para exibir itens da lista
    print(magician.title(), 'that was a great trick!')
    print("I can't wait wait to see your next trick, "+ magician.title()+".\n")
print('Thank you, everyone. that was a great magic show')

#range(inicio, parada, passo)
numbers = list(range(1,6)) #Range() pode criar uma lista de números
print(numbers)