class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(self.name , self.age)
        
class Student(Person):
    def __init__(self, name, age):
        self.sname=name
        self.sage=age
        super().__init__("Anu", age) #calling parent class init method
        
    def displayInfo(self):
        print(self.sname , self.sage)
        print(self.name , self.age)
        
s=Student("Nitin" , 23)
s.display()
s.displayInfo()                        
    