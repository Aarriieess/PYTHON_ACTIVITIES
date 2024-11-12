from abc import ABC, abstractmethod

#parent/super class
class GameCharacter(ABC): 
    @abstractmethod
    def attack(self):
        print(f"{self.name} is attacking ")

class Warrior(GameCharacter):
    def attack():
        print(f"Swings sword!")
        
class Mage(GameCharacter):
    def attack():
        print(f"Cast a Fireball!")
        
class Archer(GameCharacter):
    def attack():
        print(f"Shoots an arrow!")
        
class Healer(GameCharacter):
    def attack():
        print(f"Casts healing spell on ally!")
        

Warrior.attack()
Mage.attack()
Archer.attack()
Healer.attack()