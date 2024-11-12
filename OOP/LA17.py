import random

class Player:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0

        print(f"{self.name} attacks! It deals {self.attack_power} damage and reduces {target.name}'s HP to {target.hp}")

    def heal(self, heal_amount):
        self.hp += heal_amount
        print(f"{self.name} heals for {heal_amount} HP! Current HP is {self.hp}")

manoy = Player("Manoy", 500, 100)
albert = Player("Albert", 450, 75)

characters = [manoy, albert]


while all(character.hp > 0 for character in characters):
    if random.choice([True, False]):
        manoy.attack(albert)
    else:
        manoy.heal(50)


    if albert.hp > 0:
        if random.choice([True, False]):
            albert.attack(manoy)
        else:
            albert.heal(50)

if manoy.hp > albert.hp:
    print(f"{manoy.name} wins the battle!")
elif albert.hp > manoy.hp:
    print(f"{albert.name} wins the battle!")
else:
    print("It's a tie!")

print("GAME OVER!")