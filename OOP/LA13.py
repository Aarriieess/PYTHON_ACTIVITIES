class Animal:
    def __init__(self, name, type): 
        self.name = name
        self.type = type
        
    def describeAnimal(self):
        print(f"Name: {self.name}\nType: {self.type}\n")

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim


Dory = Fish("Dory", "Fish", True)

Dory.describeAnimal()
print(Dory.can_swim)
