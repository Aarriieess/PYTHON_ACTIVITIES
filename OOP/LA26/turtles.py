from abc import ABC

class NinjaTurtles(ABC):
    @property
    def name(self):
        pass
    
class Leonardo(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
       return self.__alias
   
class Michael_Angelo(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
       return self.__alias
   
class Donatello(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
       return self.__alias
   
class Raphael(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
       return self.__alias
