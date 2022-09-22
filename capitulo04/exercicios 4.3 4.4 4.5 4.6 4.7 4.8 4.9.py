#Exercicio 4.3
import numbers


for x in range(1,21):
    print(x, end=', ')
    
#Exercicio 4.4
numberrs = [x * 1 for x in range(1,1000001)]

#Exercicio 4.5
print('\nMenor número é: %s'%(min(numberrs)))
print('Maior número é: %s'%(max(numberrs)))
print('Soma de todos os número é: %s'%(sum(numberrs)))

#Exercicio 4.6
for x in range(1, 20, 2):
    print(x, end=", ")

#Exercicio 4.7
mul3 = [x * 3 for x in range(1, 11)]
print()
for x in mul3:
    print(x, end=", ")
    
#Exercicio 4.8
cubo = [x ** 3 for x in range(1, 11)]
print()
for x in cubo:
    print(x, end=", ")
    
#Exercicio 4.9
cubo = [x ** 3 for x in range(1, 11)]