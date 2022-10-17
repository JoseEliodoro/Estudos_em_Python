'''
filename = 'arquivos/alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        """ 
        Para que não tenha erro ao abrir um arquivo com o tipo de escrita utf-8 utilize os 
        parametros  (encoding='utf-8') ou o (errors='ignore') 
        """
        file= f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file %s does not exist.'%filename
    print(msg)
else: #Conta o número aproximado de palavras no arquivo
    words = file.split()
    num_words = len(words)
    print('The file %s has about %d words.'%(filename, num_words))
'''

#Trabalhando com vários arquivos
def count_words(filename): #Conta o número aproximado de palavra em um arquivo
    try:
        with open(filename, encoding='utf-8') as f_obj:
            file= f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file %s does not exist.'%filename
        print(msg)
        #Caso queira que o except não execute nada use o comando pass
    else: 
        words = file.split()
        num_words = len(words)
        print('The file %s has about %d words.'%(filename, num_words))
       
filename = ['alice.txt', 'poema do cume.txt', 'siddharth.txt', 'moby_dick.txt']
for file in filename:
    count_words('arquivos/'+file)