def count_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.read()
    except FileNotFoundError:
        print("Arquivo '{}' não encontrado!")
    else:
        print(lines.lower().count(word))        
        
filenames = ['1984.txt']
for file in filenames:
    count_words('capitulo10\%s'%file, 'partido')
        