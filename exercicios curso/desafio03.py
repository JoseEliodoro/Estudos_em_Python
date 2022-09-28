print("ESCOLHA A CERVEJA PELO NUMERO")
print('1-ANTARTICA R$6.00',
      '2-SKOL R$6.50',sep="    ", end='        ')
print('3-BRAHMA R$8.20',
      '4-SOL R$8.25',sep='     ')
print('5-NORTENHA R$16.80',
      '6-PROIBIDA R$4.80',
      '7-DEVASSA R$5.90',
      '8-HEINEKEN R$9.00',sep="    ")

cerveja = int(input('Digite o número referente a cerveja: '))
q = float(input("Quantas cervejas você deseja ?"))

nome = ''
valor_cerveja = 0

if(cerveja == 1):
    valor_cerveja = 6 * q
    nome = "Antartida"
elif(cerveja == 2):
    valor_cerveja = 6.5 * q
    nome = "Skol"
elif(cerveja == 3):
    valor_cerveja = 8.2 * q
    nome = "Brahma"
elif(cerveja == 4):
    valor_cerveja = 8.25 * q
    nome = "Sol"
elif(cerveja == 5):
    valor_cerveja = 16.8 * q
    nome = "Nortenha"
elif(cerveja == 6):
    valor_cerveja = 4.8 * q
    nome = "Proibida"
elif(cerveja == 7):
    valor_cerveja = 5.9 * q
    nome = "Devassa"
elif(cerveja == 8):
    valor_cerveja = 9 * q
    nome = "Heineken"
else:
    print("Valor invalido")

print(nome,"custa",valor_cerveja,"Reais, por",q,"cerveja(s)")
