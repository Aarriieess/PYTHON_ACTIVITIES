class Hero:
    #initialize
    def __init__(self,name,role,damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    #string representation
    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Damage: {self.damage_type}"

    #method
    def team_description(self):
        return f"{self.name} plays the role of {self.role} and deals {self.damage_type} damage"

edith = Hero("Edith", "Exp", "Magic")
vexana = Hero("Vexana", "Mid", "Magic")
nolan = Hero("Nolan", "Jungle", "Magic")
claude = Hero("Claude", "Marksman", "Attack")
minotaur = Hero("Minotaur", "Tank", "Attack")

heroes=[edith,vexana,nolan,claude,minotaur]

print("My team:")
for hero in heroes:
    print(hero)
print()
print("Team description:")
for hero in heroes:
    print(hero.team_description())