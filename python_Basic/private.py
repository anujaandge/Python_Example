class Base:
    def __init__(self):
        self.a=1
        self.__b=2
        
class Dervied(Base):
    def __init__(self):
        super().__init__()
        print(self.a)
        print(self.__b) # gives runtime error
        
d=Dervied()                
    