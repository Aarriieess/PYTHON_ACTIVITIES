class ml_hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

hero1 = ml_hero("Miya", "Marksman")

print(f"Name = {hero1.name}\nRole = {hero1.role}\n")
print(f"{hero1.name} - {hero1.role}")
