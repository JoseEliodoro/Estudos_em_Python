#Exercício 9.6

from exercicios_9_4_9_5 import *


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        
    def iceCreamStand(self):
        print('Temos sorvete de:')
        for flavor in self.flavors:
            print('---%s'%flavor)
        
sabores = ['chocolado', 'flocos', 'morango', 'napolitano', 'nutela']
ice = IceCreamStand('sorveteria', 'geladas', sabores)
ice.iceCreamStand()

#Exercício 9.7
class Admin(User):
    def __init__(self, first_name, last_name, password, email, username):
        super().__init__(first_name, last_name, password, email, username)
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can get user']
        
    def show_privileges(self):
        print('Os privilégios de um admin são: ')
        for privilege in self.privileges:
            print('   {}'.format(privilege))
            
adm = Admin('jose', 'eliodoro', 984565880, 'jos@gmail.com', 'srnz')
adm.describe_user()
adm.show_privileges()