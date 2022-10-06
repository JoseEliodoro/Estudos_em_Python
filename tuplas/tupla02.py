dimensions = (200, 50)
print(dimensions[0])
#dimensions[0] = 250 #Não é possível alterar uma tupla
for dimension in  dimensions: 
    print(dimension)
    
print('Original dimensions:', dimensions)
dimensions = (400, 100) #Embora não seja possível alterar uma os elementos de uma tupla, é possível sobrescrever ela
print('Modified dimensions:', dimensions)