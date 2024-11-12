class Party:
    def __init__(self, theme, special_dish, secret_dish, main_dish):
        self.__theme = theme
        self.__special_dish = special_dish
        self.__secret_dish = secret_dish
        self.__main_dish = main_dish
        
    def printFoods(self):
        print(f"Main dish: { self.__main_dish}\nSpecial dish: {self.__special_dish}")
        self.__printSecretDish()
        
    def __printSecretDish(self):
        print(f"Secret dish: {self.__secret_dish}\n")
    
christmas = Party("Christmas Party", "Karne ng reindeer", "Balbas ni Santa Claus", "Ham")
halloween = Party("Halloween Party", "Kuko ng zombie", "Pakpak ng manananggal", "Chocolates")
newYear = Party("New Year Party", "Pinakuluang 5 star", "Ginataang sintuon ni hudas", "12 bilog na prutas")


christmas.printFoods()
halloween.printFoods()
newYear.printFoods()