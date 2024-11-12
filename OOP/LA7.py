class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        

car1 = Car("Missyoubibi", "Black")
print(f"Original Car1 brand and color: {car1.brand} - {car1.color}")
car1.color = "Red"
print(f"Updated Car1 brand and color: {car1.brand} - {car1.color}")

car2 = Car("Nissin", "White")
print(f"Original Car2 brand and color: {car2.brand} - {car2.color}")