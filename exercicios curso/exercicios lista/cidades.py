import os
citys, verify, cont = [], False, 0

while(verify != True):
    nameCity= input('DIGITE O NOME DA CIDADE_%i: ' %cont)
    citys.append(nameCity)
    test = input('DESEJA CONTINUAR [S/N]? ')
    if(test == 'N' or test == 'n'):
        verify = True
    cont += 1
    os.system('cls')

for nameCity in citys:
    print(nameCity)