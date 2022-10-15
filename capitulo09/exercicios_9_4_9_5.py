#Exercício 9.4
import random


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type): #Construtor
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    def describe_restaurant(self): #Métododo que exibe o nome e o tipo de culinaria do restaurante
        print('O restaurante {} server comidas {} para seus clientes'.format(self.name.title(), self.cuisine))
    
    def open_restaurant(self): #Método que informa que o restaurante está aberto
        print('O restaurante esta aberto')

    def set_number_served(self, customer): #Método que define quantos clientes foram atendidos
        self.number_served = customer
        
    def increment_number_served(self, customers): #Método que incrementa a quantidade passada a quantidade já estabelecida
        self.number_served += customers
        
"""         
restaurant = Restaurant('lazerão', 'nordestina')
print('Números de clientes atendidos:',restaurant.number_served)
restaurant.number_served = 5
print('Números de clientes atendidos:',restaurant.number_served)
restaurant.set_number_served(10)
print('Números de clientes atendidos:',restaurant.number_served)
restaurant.increment_number_served(7)
print('Números de clientes atendidos:',restaurant.number_served)
 """


#Exercício 9.5

class User():
    def __init__(self, first_name, last_name, password, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.username = username
        self.login_attempts = 0
        
    def describe_user(self): #Método que exibe as informação do usuário
        print('\nO usuário: {} está cadastrado no email {}'.format(self.username, self.email),
              '\nSeu nome é %s e sua senha é %s.'%(self.first_name.title() +" "+ self.last_name.title(), self.password))
        
    def increment_login_attempts(self): #Método que conta as tentativa de login do usuário
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
    
    
""" 
user = User('madara', 'uchira', 'hashirama', 'tsukiomi@gmail.com', 'matador de dinossauro')
x = random.randint(1, 15)
c=0
print(user.login_attempts)
while c <= x:
    user.increment_login_attempts()
    c +=1
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
"""