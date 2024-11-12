class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    
    def introduce(self, function):
        def intro(*args, **kwargs):
            print("Introducing...")
            function(*args, **kwargs)
            print("This character is amazing!...")
    
jin = TekkenCharacter("Jin", "Super Blow Jab")

@jin.introduce
def character_intro():
    print(f"I am {jin.name} and I can use {jin.ability}")
character_intro() 



