import aula16
from aula16 import print_ab as tq 
#utilizado para importar uma função e dar um apilidio para ela

n1 = float(input('Informe um número real: '))
n2 = float(input('Informe outro número real: '))
print(f"{n1} + {n2} = {aula16.soma(n1,n2)}")

tq() #apelido que representa a função importada
