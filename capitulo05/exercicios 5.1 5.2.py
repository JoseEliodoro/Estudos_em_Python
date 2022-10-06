#Exercício 5.1
car = 'subaru'
print("Is car = 'subaru'? I predict True.", car == 'subaru')
print("Is car = 'audi'? I predict True.", car == 'audi')

numbers = list(range(0, 100))

for number in numbers:
    cont = 0
    
    for x in range(1, number + 1):
        if(number % x == 0):
            cont += 1
        if(cont == 3):
            break
            
    if(cont == 2):
        print(number, 'é primo')
        
