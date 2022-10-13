'''
n = int(input('Digite um número inteiro: '))

verify = 0

for x in range(1, n+1):

    if (n % x == 0):
        verify += 1

if(verify == 2):
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')

for n in range(100):
    verify = 0

    for x in range(1, n+1):

        if (n % x == 0):
            verify += 1

    if(verify == 2):
        print(n)

a = 0
while (a < 10):
    print(a)
    a += 1

nota = int(input('Entre com a nota: '))
while nota > 10:
    nota= int(input('Entre com a nota: '))
'''
a, b, c, d = 11, 11, 11, 11
while (a > 10 or b > 10 or c > 10 or d > 10):
    if a > 10:
        a = int(input('Primeiro bimestre: '))
    if b > 10:
        b = int(input('Segundo bimestre: '))
    if c > 10:
        c = int(input('Terceiro bimestre: '))
    if d > 10:
        d = int(input('Quarto bimestre: '))
    
if ((a + b + c + d)/4 < 7):
    print(f'Sua nota foi {(a + b + c + d)/4}, Você foi reprovado!')
else:
    print(f'Sua nota foi {(a + b + c + d)/4},Você está aprovado!')