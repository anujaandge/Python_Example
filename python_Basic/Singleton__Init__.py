class Singleton:
    _insatace=None
    def __new__(cls, *args, **kwargs):
        if not cls._insatace:
            cls._insatace=super(Singleton, cls).__new__(cls)
            
        return cls._insatace
    
    def __init__(self, value):
        if not hasattr(self, 'initialized'):
            self.value= value
            self.initialized=True
            
s1=Singleton(10)
s2=Singleton(20)

print(s1== s2)
print(s1.value)
print(s2.value)            