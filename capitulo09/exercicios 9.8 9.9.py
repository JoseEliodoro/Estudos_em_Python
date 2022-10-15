#Exercício 9.8
from exercicios_9_4_9_5 import User

class Admin(User):
    def __init__(self, first_name, last_name, password, email, username):
        super().__init__(first_name, last_name, password, email, username)
        self.privileges = Privileges()
        
    
            
class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can get user']
    
    def show_privileges(self):
        print('Os privilégios de um admin são: ')
        for privilege in self.privileges:
            print('   {}'.format(privilege))
    
adm = Admin('jose', 'eliodoro', 984565880, 'jos@gmail.com', 'srnz')
adm.describe_user()
adm.privileges.show_privileges()

#Exercício 9.9

""" Adicinei o método upgrade_battery() na classe Battery no arquivo class04,
esse método define a bateria para 85
"""

