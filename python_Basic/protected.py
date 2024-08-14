class Base:
    def __init__(self):
        self._a=2
        
class Derived(Base):  
    def __init__(self):
        super().__init__()
        print("protected member from base class: ",self._a)
        self._a=3
        print("modified protected member of base class outside the class: ",self._a)
        
        
O=Derived()
A=Base()
print(O._a)
print(A._a)              