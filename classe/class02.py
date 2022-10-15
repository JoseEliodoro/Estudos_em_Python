class Car(): #Uma tentativa simples de representar um carro.
    
    def __init__(self, make, model , year): #Inicializa os atributos que descrevem um carro.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self): #Devolve um nome descritivo, formatado de modo elegante
        long_name = '%d %s %s'%(self.year, self.make, self.model)
        return long_name
    
    def read_odometer(self): #Exibe uma frase que mostra a milhagem do carro.
        print('This car has %d miles on it.'%self.odometer_reading)
        
    def update_odometer(self, mileage): #Define o valor do atributo através de um método
        
        if(mileage < self.odometer_reading): #Impede que coloque um valor menor que o já inserido
            print("You can't roll back an odometer!")
        self.odometer_reading = mileage
    
    def increment_odometer(self, miles): #Soma a quantidade passado com a já definida
        self.odometer_reading += miles
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23 #Modificação de atributo de forma direta
my_new_car.read_odometer()
my_new_car.update_odometer(77)
my_new_car.read_odometer()
my_new_car.update_odometer(13)

print()
my_used_car = Car('subaru', 'outback', 2014)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()