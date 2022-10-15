class Battery():
    def __init__(self, battery_size=70): #Inicializa os atributos da bateria.
        self.battery_size = battery_size
    
    def describe_battery(self): #Exibe uma grase que descreve a capacidade da bateria.
        print('This car has a %.2f-kWh battery.'%self.battery_size)
        
    def get_range(self): #Exibe uma grase sobre a distância que o carro é capaz de percorrer com essa bateria.
        if self.battery_size == 70:
            range = 240
        elif(self.battery_size == 85):
            range = 270
        message = 'This car can go approximately %s miles on full charge.'%range
        print(message)
        
    def upgrade_battery(self):
        if(self.battery_size != 85):
            self.battery_size = 85
        else:
            print('bateria já está em 85!')