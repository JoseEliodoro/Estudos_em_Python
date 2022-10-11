import math #Importando biblioteca padrão do python para funções matematicas

raiz = math.sqrt(9) 
#O método .sqrt() extrai a raiz de um número
pi = math.pi
#O parametro .pi retorna o valor do número de pi
radianos = math.radians(60)
#O método .radians() Converte o angulo 'numero' de graus para radiano.
cosseno = math.cos(radianos)
#O método .cos() retorna o cosseno do número em radiano.
seno = math.sin(math.radians(30))
#O método .sin() retorna o seno do número em radiano.
tangente = math.tan(math.radians(45))
#O método .tan() retorna a tangente do número em radiano.
hipotenosa = math.hypot(3, 4)
#O método .hypot(x, y) retorna a hipotenusa dos números (catetos) fornecidos.

print("raiz de 9 é", raiz)
print("pi é", pi)
print("60º em radianos é %.2f"%(radianos))
print("cosseno de 60 é %.2f"%(cosseno))
print("seno de 30 é %.2f"%(seno))
print("tangente de 45 é %.2f"%(tangente))

#Site com todos os métodos e atributos dessa biblioteca
#https://docs.python.org/3.5/library/math.html?highlight=math#module-math