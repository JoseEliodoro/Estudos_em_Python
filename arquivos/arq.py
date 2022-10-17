filename = 'arquivos/pi_digits.txt'
#Analisando todo o arquive de uma vez
""" 
with open(filename) as file_object:
    '''
    Comando open() é responsavel por abrir um arquivo, referente ao caminho especificado 
    o retorno dessa função é um objeto que representa esse arquivo
    
    o comando with fecha o arquivo após a utilização dele no bloco que o segue
    '''
    contents = file_object.read() #Método responsavel por ler todo o conteúdo do arquivo
print(contents)
 """

#Analisando uma linha de cada vez
""" 
with open(filename) as file_object:
    
    for line in file_object: #Bloco de repetição para cada uma das linhas semelhante a uma lista, cada line possue uma quebra de linha no final
        print(line.strip()) 
"""
        
with open(filename) as file_object:
    
    lines = file_object.readlines() #Método que retorna uma lista contendo cada uma da linhas
    
for line in lines:
    print(line.rsplit())
    