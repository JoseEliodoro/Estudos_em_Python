class Dog(): #Uma tentativa de modelar um cahorro
    
    def __init__(self, name, age): #Inicializa os atributos name e age
        self.name = name.title()
        self.age = age
    
    def sit(self): #Simula o cachorro sentando em resposta a um comando
        print(self.name +' is now sitting.')
    
    def roll_over(self): #Simula um cachorro rolando em resposta a uma comando
        print(self.name + ' rolled over!')
        
    
#Instânciando uma classe 
my_dog = Dog('willie', 6)

#Chamando atributos
print("My dog's name is "+ my_dog.name.title() +".")
print("My dog is "+ str(my_dog.age) +"years old.")

#chamando métodos
my_dog.sit()
my_dog.roll_over()