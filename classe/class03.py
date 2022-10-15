class Car(): #Uma tentativa simples de representar um carro.
    
    def __init__(self, make, model , year): #Inicializa os atributos que descrevem um carro.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self): #Devolve um nome descritivo, formatado de modo elegante
        long_name = '%d %s %s'%(self.year, self.make.title(), self.model.title())
        return long_name
    
    def read_odometer(self): #Exibe uma frase que mostra a milhagem do carro.
        print('This car has %d miles on it.'%self.odometer_reading)
        
    def update_odometer(self, mileage): #Define o valor do atributo através de um método
        
        if(mileage < self.odometer_reading): #Impede que coloque um valor menor que o já inserido
            print("You can't roll back an odometer!")
        self.odometer_reading = mileage
    
    
    def increment_odometer(self, miles): #Soma a quantidade passado com a já definida
        self.odometer_reading += miles
        
"""Criando nova classe EletricCar que herdara a classe Car"""
from class04 import Battery #Importando classe battery

class ElectricCar(Car): #Representa aspectos específicos de veículos elétricos.
    
    def __init__(self, make, model, year): #Inicializa os atributos da classe-pai em seguida os dele próprio
        super().__init__(make, model, year) #diz para iniciar o construtor de sua classe pai
        self.battery= Battery() #Instância de classe como atributo
        
        
    def fill_gas_tank(): #Carros elétricos não possuem tanques de gasolina
        print("this car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()