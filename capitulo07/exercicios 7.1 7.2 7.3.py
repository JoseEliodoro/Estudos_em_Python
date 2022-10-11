#Exercício 7.1
car = 'subaru' #input('Qual tipo de carro você deseja: ')

print('Deixe-me ver se consigo um %s para você'%car.title())

#Exercício 7.2
qtd_lugar = 8 #int(input('Informe quantas pessoas estão no seu grupo: '))
if(qtd_lugar > 8):
    print('Vocês terão que aguardar uma mesa ficar disponivel.')
else:
    print('Sua mesa já está pronta.')
    
#Exercício 7.3
number = int(input('Digite um número: '))

if(number%10 == 0):
    print(number, 'é multiplo de 10')
else:
    print(number, 'não é multiplo de 10')