from abc import ABC, abstractmethod
class Demo(ABC):
    @abstractmethod
    def method1(self):
        print("Abstrct method")
        
    def method2(self):
        print("Concrete method")
        
#obj=Demo()  cannot create instance of abstract class it will show error

class concreteclass(Demo):
    def method1(self):
        #return super().method1() 
        print("method of concrete class" )
        
obj=concreteclass()
obj.method1()
obj.method2()               
    