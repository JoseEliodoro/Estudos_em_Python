#Exercício 3.1
names = ['josé', 'carlos', 'EliOdoro', 'SANTANA']

for x in names:
    print(x.title())

#Exercício 3.2
for x in names:
    print('Bom dia, {}'.format(x.title()))
    
#Exercício 3.3
vehicle = ['Moto', 'picaqe', 'fusca']
print('Eu quero ter uma {} até 2024'.format(vehicle[0]))
print('Desejo ter %s quando tiver em outro pais' %(vehicle[1]))
print('Ter um',vehicle[2],'quando ficar rico')