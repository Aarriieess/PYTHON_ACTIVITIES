import random

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, target):
        target.hp -= self.power
        print(f"{self.name} attacked {target.name} and dealt {self.power} damage.")

    def special_move(self):
        print(f"{self.name} uses a special skill.\n")


class Warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.double_damage = False

    def special_move(self, target):
        if self.double_damage:
            target.hp -= self.power
            print(f"{self.name} attacked {target.name} with DOUBLE power and dealt {self.power} damage.")
            self.power /= 2
            self.double_damage = False
        else:
            target.hp -= self.power
            print(f"{self.name} attacked {target.name} and dealt {self.power} damage.")
            self.power *= 2
            self.double_damage = True

    def defend(self, attacker):
        damage_taken = attacker.power / 2
        self.hp -= damage_taken
        print(f"{self.name} reduced the damage taken from {attacker.name}'s attack by {damage_taken}.")


class Mage(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
            
    def special_move(self, target):
        target.hp -= self.power
        print(f"\"{self.name} cast Fireball!\" and reduces {target.name}'s health by {self.power}.")

    def defend(self, attacker):
        damage_taken = attacker.power / 2
        self.hp -= damage_taken
        print(f"{self.name} reduced the damage taken from {attacker.name}'s attack by {damage_taken}.")


class Archer(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
            
    def special_move(self, target):
        target.hp -= self.power
        print(f"\"{self.name} shoots a Piercing Arrow!\" and ignores {target.name}'s defense, causing direct damage.")

    def defend(self, attacker):
        damage_taken = attacker.power / 2
        self.hp -= damage_taken
        print(f"{self.name} reduced the damage taken from {attacker.name}'s attack by {damage_taken}.")


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
            
    def special_move(self):
        heal_amount = random.randint(20, 50)
        self.hp += heal_amount
        print(f"\"{self.name} roars and gains extra health!\" and increases its health by {heal_amount}.")
        


pantheon = Warrior("Pantheon", 500, 100)
brand = Mage("Brand", 250, 200)
ashe = Archer("Ashe", 300, 150)
dragon = Monster("Dragon", 1000, 100)

characters = [pantheon, brand, ashe]

for hero in (characters):
    print(f"{hero.name}:\nHp: {hero.hp}\nAttack: {hero.power}\n")

while len(characters) > 0 and (pantheon.hp > 0 or brand.hp > 0 or ashe.hp > 0 or dragon.hp > 0):
    
    attacking_hero = random.choice(characters)
    attacking_hero.special_move(dragon)
    print(f"{dragon.name} current hp: {dragon.hp}\n")
    
        
    if dragon.hp <= 0:
        print(f"{dragon.name} died in the battle")
        break
            
    if dragon.hp > 0:
        dragon.attack(attacking_hero)
        print(f"{attacking_hero.name} current hp: {attacking_hero.hp}\n")
        
    if attacking_hero.hp > 0:
            attacking_hero.defend(dragon)
            
    if attacking_hero.hp <= 0:
            attacking_hero.hp = 0
            print(f"{attacking_hero.name} died in the battle\n")
            characters.remove(attacking_hero)
            

print("\nGAME OVER!")

if not characters:
    print("The Dragon has defeated the heroes!")
elif dragon.hp <= 0:
    print("The heroes have defeated the Dragon!")
