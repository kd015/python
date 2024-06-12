class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " ! "
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(Self):
        return "Diseal or Petrol"
    
class ElectriCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(Self):
        return "Electric Charge"
    

my_tesla = ElectriCar("Tesla", "Model S", "85kWh")
#print(my_tesla.__brand)

safari = Car("Tata", "Safari")

print(Car.total_car)
