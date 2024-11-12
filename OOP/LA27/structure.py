from abc import ABC, abstractmethod

class Pagong(ABC):
    @abstractmethod
    def langoy(self):
        pass
    
    
class Donnatello(Pagong):
    def langoy(self):
        print("Ninja Turtle")
        
if __name__ == "__main__":
    ping = Donnatello()
    ping.langoy()