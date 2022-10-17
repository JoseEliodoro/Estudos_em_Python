
import random

city = [(4,5),(5,4),(9,3),(5,4)]
ra = random.sample(city, k=4)
print(ra)
print('-' in '15*44151*')
try:
    print(8/0)
    print(int('a'))
except ValueError:
    print('int para a')
except ZeroDivisionError:
    print('divisão por zero')