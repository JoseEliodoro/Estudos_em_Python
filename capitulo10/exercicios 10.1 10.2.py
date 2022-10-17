#Exercício 10.1
filename = 'capitulo10\learning_python.txt'
with open(filename) as file_object:
    
    #print('Lendo arquivo de uma vez:\n'+ file_object.read())
    
    print('\nLendo arquivo e percorrendo o objeto:')
    for line in file_object:
        print('   '+ line.strip())
        
    #lines = file_object.readlines()

#print('\nArquivo armazenado numa lista:', lines)

#Exercício 10.2
with open(filename) as file_object:
    print("\nSubstituindo a palavra 'Python' por 'C':")
    for line in file_object:
        print("   "+line.replace('Python', 'C').strip())