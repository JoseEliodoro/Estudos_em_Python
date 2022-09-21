#Exercício 3.4
convi = ['bolsonaro', 'raquel', 'lula']

for x in convi:
    print(f'Sr(a) {x.title()}, está convidado para jantar')
    
#Exercício 3.5
print(f'O Sr(a) {convi[1].title()} não poderá comparecer')
convi[1] = 'ciro'
print(f'Porém o Sr(a): {convi[1].title()} virá em seu lugar')

#Exercício 3.6
print('Encontrei uma mesa maior, então convidei mais pessoas')
convi.insert(0, 'cabo daciolo')
convi.insert(2, 'marina')
convi.append('dilma')

for x in convi:
    print(f'Sr(a) {x.title()}, está convidado para jantar')
    
#Exercício 3.7
print("Só posso convidar 2 pessoas")

for a in range(4):
    b = convi.pop()
    print('Desculpa %s, mas não posso convidalo'%b)
        

for x in convi:
    print('Sr: %s, você ainda tá convidado'%x)
    
del(convi[0])
del(convi[0])
print(convi)