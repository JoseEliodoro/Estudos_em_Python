filename = 'arquivos\pi_100000_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

string = ''
for line in lines:
    string += line.rstrip()

birthday = input('Enter your birthday, in the from mmddyy: ')
if birthday in string:
    print('Your birthday appears in the first 100000 digits of pi!')
else:
    print('Your birthday does not appear in the first 100000 digits of pi.')
print(len(string))