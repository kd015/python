class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " ! "
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectriCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    

my_tesla = ElectriCar("Tesla", "Model S", "85kWh")
#print(my_tesla.__brand)
print(my_tesla.get_brand())

#variable ko 2 underscore lgane ke wo private ho jata hai => encapsulate ho gya, class ke under ho jayega but object se nhi, log agr chahte hai to, method banana hoga 
   