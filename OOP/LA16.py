class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        return f"{self.brand} {self.model} is operating!"

    def info(self):
        return f"{self.brand} - {self.model}"
        
class WashingMachine(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        return f"Washing clothes!"

class Refrigerator(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        return f"Keeping food cold!"

class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def operate(self):
        return f"Heating food!"

# Create instances of appliances
washingMachine = WashingMachine("LG", "Objet WashTower")
ref = Refrigerator("Samsung", "SBS Family Hub")
microwave = Microwave("Panasonic", "NN-SN65KB")

appliances = [washingMachine, ref, microwave]

def recursion(appliances):
    if len(appliances) == 0:
        return ""
    else: 
        return appliances[0].operate() + "\n" + recursion(appliances[1:])

print(recursion(appliances))

# for appliance in (washingMachine, ref, microwave):
#     print("\n")
#     print(appliance.operate())
#     print(appliance.info())