#Tratamento de erro para divisão por zero
try: 
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input('Sedond number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
        
    """ 
    try-except-else
    Por padrão o único código que pode estar no bloco try é aquele que gera a exceção.
    Caso exista um código adicionau que acontece caso o bloco try tiver exito coloque no bloco else.
    No bloco except coloque o código que será executado caso a exeção aconteça.
    """