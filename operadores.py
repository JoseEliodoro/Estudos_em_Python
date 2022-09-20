a = 10 
b = 2

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
divisao_inteiro = a // b
exponenciacao = a ** b

print(a,"+",b,"=",soma)
print(a,"-",b,"=",subtracao)
print(a,"*",b,"=",multiplicacao)
print(a,"/",b,"=",divisao)
print(a,"%",b,"=",resto)
print(a,"//",b,"=",divisao_inteiro)
print(a,"**",b,"=",exponenciacao)

print(a,"<",b,"=",a < b)
print(a,">",b,"=",a > b)
print(a,"<=",b,"=",a <= b)
print(a,">=",b,"=",a >= b)
print(a,"!=",b,"=",a != b)
print(a,"==",b,"=",a == b)

print('Soma = {soma} \n'
      'subtração = {sub} \n'
      'multiplicação {multiplicacao}'
      'divisao = {divisao}'.format(sub=subtracao,
                                             soma=soma,
                                             multiplicacao=multiplicacao,
                                             divisao=divisao))

# and -> e
# or  -> ou
# not -> não