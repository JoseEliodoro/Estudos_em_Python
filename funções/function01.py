""" 
Argumentos posicionais são quando colocamos eles na mesma ordem
com a qual eles foram declarados na funcão
"""
def describe_pet(animal_type, pet_name): #Exibe informaçãos sobre um animal de estimação
    print('\nIhave a %s.'%animal_type)
    print("My %s's name is %s"%(animal_type, pet_name.title()))
describe_pet('hamster', 'harry')

""" 
Argumentos nomeados funcionam como nome valor, em que ele são associados diretamente ao nome do argumento que inserimos, desse jeito a ordem dos argumentos pouco importa
"""
describe_pet(pet_name='jeff', animal_type='dog')

#Inserindo default as funções
def sum(a = 1, b= 5):
    return a + b

print(sum())

def biuld_person(first_name, last_name, age = ''):
    person = {'first': first_name, 'last': last_name}
    if age: #Verifica se uma string está vazía
        person['age'] = age
    return person

musician = biuld_person('jose', "carlo", 19)
print(musician)
musician2 = biuld_person('eliodoro', 'santana')
print(musician2)