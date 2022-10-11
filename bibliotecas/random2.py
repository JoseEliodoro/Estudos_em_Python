import random # necessário para utilizar o módulo random
 
print(random.random()) #Gera número pseudoaleatório de 0.0 a 1.0
print(random.uniform(1, 10)) #Gera número pseudoaleatório de x a y
print(random.randint(1, 55)) #Gera número pseudoaleatório de x a y de forma decimal

cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores)) #Gera um dos elementos contidos na lista

cartas_de_baralho = ['ás de copas', 'ás de espadas', 'ás de paus', 'ás de ouro']
random.shuffle(cartas_de_baralho) #coloca uma lista em uma ordem aleatória
print(cartas_de_baralho)

city = [(4,5),(5,4),(9,3),(5,4)]
ra = random.sample(city, k=4) #Embaralha os elementos mas não muda a lista original
print(ra)