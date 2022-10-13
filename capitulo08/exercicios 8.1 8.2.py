#Exercício 8.1
def display_message(user):
    return 'Olá %s, eu estou aprendendo funções'%user.title()

print(display_message(input('Digite seu nome: ')))


#Exercício 8.2
def favorite_book(title_book):
    print('Um do meus livros favoritos é '+ title_book.title())
    
favorite_book(input("Qual seu livro favorito: "))