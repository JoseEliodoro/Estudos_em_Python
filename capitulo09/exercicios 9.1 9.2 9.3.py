#Exercício 9.1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        print('O restaurante {} server comidas {} para seus clientes'.format(self.name.title(), self.cuisine))
    
    def open_restaurant(self):
        print('O restaurante esta aberto')

restaurant = Restaurant('lazerão', 'nordestina')
print('O nome do restaurante é', restaurant.name)
print('servem comida '+ restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#Exercício 9.2
restaurant01 = Restaurant('brazero', 'pizza')
restaurant02 = Restaurant('outback', 'americana')
restaurant03 = Restaurant('djapa', 'japonesa')

#Exercício 9.3
class User():
    def __init__(self, first_name, last_name, password, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.username = username
        
    def describe_user(self):
        print('\nO usuário: {} está cadastrado no email {}'.format(self.username, self.email),
              '\nSeu nome é %s e sua senha é %s.'%(self.first_name.title() +" "+ self.last_name.title(), self.password))
        
user01 = User('jose', 'eliodoro', 'jose123', 'jose@gmail.com', 'srnz')
user02 = User('gildo', 'eliodorio', '0794', 'gildo@gmail.com', 'cabo_gildo')
user03 = User('madara', 'uchira', 'hashirama', 'tsukiomi@gmail.com', 'matador de dinossauro')
user01.describe_user()
user02.describe_user()
user03.describe_user()