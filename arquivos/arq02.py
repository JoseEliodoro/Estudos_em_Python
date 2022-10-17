fileName = 'arquivos\pi_digits.txt'
with open(fileName) as file_object:
    
    lines = file_object.readlines()

string = " "
for line in lines:
    string += line.strip()
    
print(string)
with open('recursos do livro\ehmatthes-pcc_2e-078318e\chapter_10/pi_million_digits.txt') as file_object:
    
    lines = file_object.readlines()

string = " "
for line in lines:
    string += line.strip()
    
print(string[:53]+'...')