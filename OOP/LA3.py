class ml_hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def heroObject(self):
        return f"{self.name} is {self.role} hero."
    
    def __str__(self):
        return f"{self.name} is {self.role} hero."

        

hero1 = ml_hero("Miya", "Marksman")
hero2 = ml_hero("Layla", "Marksman")

print(f"Name: {hero1.name} - Role: {hero1.role}")
print(ml_hero.heroObject(hero1))
print(hero1)
print()
print(f"Name: {hero2.name} - Role: {hero2.role}")
print(ml_hero.heroObject(hero2))
print(hero2)

