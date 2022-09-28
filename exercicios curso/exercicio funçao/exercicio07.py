""" #Exercício 01
def firstFuction():
    print('Minha primeira função')
firstFuction()

#Exercício 02
def info(n, a):
    return '{nome} possui {idade} anos.'
name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))
print(info(name, age))

#Exercício 03
def mult(x, y):
    return x * y
print(mult(5, 6))

#Exercício 04
def double(x):
    return x * 2
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o primeiro número: '))
print(double(max(a, b, c)))
"""
#Exercício 05
def addList(name, lista):
    lista.append(name)

def viewName(l = {}):
    for x in range(5):
        print('O %dº nome é %s'%(x, l[x]))
        
lista = list()         
for i in range(5):
    addList(input('Digite um nome: '), lista)
    
viewName(lista)