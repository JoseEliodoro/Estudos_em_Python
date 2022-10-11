aliens = list()

for alien in range(0, 30):
    aliens.append({ #Criando uma lista de dicionários
        'color': 'green',
        'points': '5',
        'speed': 'slow'
    })
for alien in aliens[:5]:
    print(alien)
    
print('Total number of aliens: %d'%(len(aliens)))

for alien in aliens[:3]:
    if(alien['color'] == 'green'):
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'

    
for alien in aliens[:5]:
    print(alien)
""" 
Não aumente tanto o nível de profundidade de listas de 
dicionários, caso faça isso, lembresse que concerteza existe forma mais simples de solucionar o problema 
"""

#Dicionário de dicionário

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'eisntein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}"
          f"\nFull name: {user_info['first'] + user_info['last']}"
          f"\nLocation: {user_info['location']}")