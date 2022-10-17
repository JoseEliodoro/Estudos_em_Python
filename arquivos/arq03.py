filename = 'arquivos\programming.txt'
#Escrevendo num arquivo de texto
with open(filename, 'w') as file_object:
    #Essa função já cria automaticamente o arquivo caso não exista
    """ 
    O segundo argumento pode ser as seguintes strings
    'r' -> abrir em modo de leitura, só permite pegar o conteúdo
    'w' -> abrir em modo de escrita, subrescreve o conteúdo
    'a' -> abrir em modo de concatenação, pode juntar os texto
    'r+' -> abrir em modo de leitura e concatenação
    Caso o argumento seja omitido o padrão é de leitura
    """
    file_object.write('I love proframming.\n')
    file_object.write('I love creating new games.\n')
    """ for line in file_object:
        print(line) """

#Concatenando em um arquivo de texto    
with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.zn')