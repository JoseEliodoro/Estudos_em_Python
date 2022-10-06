alien_0 = {'color': 'green','points': 5} #estrutura de um dicionário

print(alien_0['color']) #Dicionarios em python não aceitam o conjunto chave valor como um objeto igual no JS
#Nota alien_0.color não funciona
print(alien_0['points'])

alien_0['x_position'] = 0 #Add novo chave-valor no dicionário
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow' #Modifica valor do dicionário

del(alien_0['points']) #Remove uma chave do dicionário
print(alien_0)