class Chicken:
    def __init__(self, chicken, ingridient1, ingridient2, ingridient3, ingridient4):
        self.__chicken = chicken
        self.__ingridient1 = ingridient1
        self.__ingridient2 = ingridient2
        self.__ingridient3 = ingridient3
        self.__ingridient4 = ingridient4

    def __str__(self): 
        return f"Meat: {self.__chicken}\n1st Ingridient: {self.__ingridient1}\n2nd Ingridient: {self.__ingridient2}\n3rd Ingridient: {self.__ingridient3}\n4th Ingridient: {self.__ingridient4}\n"

    def getChicken(self):
        return self.__chicken
    
    def setChicken(self, chicken):
        self.__chicken = chicken
    
Fried_Chicken = Chicken("Chicken Breast", "Egg", "Crispy Fry", "Bread Crumbs", "Pepper")
print(Fried_Chicken.getChicken())

Fried_Chicken.setChicken("Chicken Thigh")
print(Fried_Chicken.getChicken())