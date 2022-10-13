#Exercício 8.6
def city_country(city_name, country):
    return city_name.title() +', '+ country.title()

print(city_country('Santiago', 'chile'))
print(city_country('Recife', 'brASiL'))
print(city_country('tokyo', 'japão'))

#Exercício 8.7
def make_album(artista, titulo, qtd_faixa = None):
    album = {'artista': artista.title(), 'título': titulo.title()}
    if qtd_faixa:
        album['faixas'] = qtd_faixa
    
    return album

print(make_album('jose', 'o melhor do brega'))
print(make_album(titulo='O conTADOR De HiSTÓriAs',artista='dk47',  qtd_faixa=3))
print(make_album(titulo='favela vive',artista='ADL',  qtd_faixa=4))

#Exercício 8.8
while True: 
    print("\nCaso que para de informa aparte 'q'")
    album = input('Informe o título do álbum: ')
    if album =='q':
        break
    artista = input('Informe o nome do artista: ')
    if album =='q':
        break
    print(make_album(artista, album))