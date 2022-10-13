#Exercício 8.3,8.4
def make_shirt(len_shirt = 'g', message_shirt = 'eu amo python'):
    print(f"Uma camisa tamanho {len_shirt.upper()} com a mensagem {message_shirt.title()} será feita")
    
make_shirt('p', 'Berserk')
make_shirt(message_shirt='eu sou o melhor', len_shirt='m')

make_shirt()
make_shirt(message_shirt='eu sou foda')

def describe_city(city_name, country = 'brasil'):
    print(city_name.title(),'está localizada no {}'.format(country.title()))
    
describe_city('Igarassu')
describe_city(country='canadá', city_name='toronto')
describe_city('kyoto', 'japão')