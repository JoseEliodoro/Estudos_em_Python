#Exercício 8.12
def make_sandwiche(ingredientes):
    print('um sandwiche com', end='')
    result = ''
    for ingrediente in ingredientes:
        result += ', '+ ingrediente
    print(result)
    
make_sandwiche(['tomate', 'cebola', 'pimentão', 'hamburguer', 'maionese', 'cketchup'])
make_sandwiche(['frango', 'cebola', 'pimentão', 'mortadela', 'queijo', 'cketchup'])
make_sandwiche(['frango', 'cebola', 'alface', 'bacon', 'maionese', 'mostarda'])

#Exercício 8.13
def build_profile(first, last, **aparents):
    person = {'first_name': first, 'last_name': last}
    for k, v in aparents.items():
        person[k] = v
    return person

print(build_profile(last='carlos', first='jose', age=19, height=1.70, eye_color='marrow'))

#Exercício 8.14

def make_car(fabricante, modelo, **ap):
    car = {'fabricante': fabricante, 'modelo': modelo}
    for k, v in ap.items():
        car[k] = v
    return car
car = make_car('subaru', 'outback',color='blue', tow_package=True)
print(car)