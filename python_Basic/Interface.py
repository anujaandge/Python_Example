# from abc import ABC, abstractmethod
# #creating interface
# #Formal Interface Example
# class DemoInterface(ABC):
#     @abstractmethod
#     def method1(self):
#         print("Abstrct method 1")
    
#     @abstractmethod
#     def method2(self):
#         print("Abstrct method 2")

# #implementing interfcae        
# class ConcreteClass(DemoInterface):
#     def method1(self):
#         print("This is method 1 of concrete class")
#         return super().method1()
#     def method2(self):
#         print("This is method 2 of concrete class")
#         return super().method2() 
               
# obj=ConcreteClass()
# obj.method1()             
# obj.method2()   


#Type 2
#Informal Interface
#in this type no need to implement all method of interfcae
class ExampleInterface:
    def display(self):
        pass
    
    def show(self):
        pass
    
class newClass(ExampleInterface):
    def display(self):
        print("This is newclass implemented by Interface")
        
obj1=newClass()
obj1.display()        
        