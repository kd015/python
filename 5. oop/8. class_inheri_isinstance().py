class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " ! "
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(Self):
        return "Diseal or Petrol"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectriCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(Self):
        return "Electric Charge"
    

my_tesla = ElectriCar("Tesla", "Model S", "85kWh")

my_car = Car("Tata", "Safari")
#Car('Tata','Nexon')

print(isinstance(my_tesla, ElectriCar))
print(isinstance(my_tesla, Car))

