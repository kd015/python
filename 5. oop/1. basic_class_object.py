#Attribute = Variable, Instance = koi ek example, init = constructor, class = ke pas first letter capital, self
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)