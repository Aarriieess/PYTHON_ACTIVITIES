class Vehicle:
    def __init__(self, brand, model, fuel_type): 
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        
    def describeVehicle(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nFuel type: {self.fuel_type}\n")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

Misubibi = Car("Misubibi", "L300", "Gas")
Honda = Motorcycle("Honda", "CB650R", "Gas")

Misubibi.describeVehicle()
Honda.describeVehicle()
