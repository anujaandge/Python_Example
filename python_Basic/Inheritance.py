class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def Display(self):
        print(self.name, self.id) 
        
p=Person('Anu',1)
p.Display()         

class Emp(Person):
    def Print_emp(self):
        print(self.name,self.id)
class Emp1(Person):
    def __init__(self, name, id, age):  #adding new attribute to child class
        self.ename=name
        self.eid=id
        self.age=age
        super().__init__(name, id)        
    def DisplayInfo(self):
        print(self.ename, self.eid, self.age) 
emp=Emp("nitin",2)
emp.Display()
emp.Print_emp() 
emp1=Emp1("Anu", 1, 23)         
emp1.Display()
emp1.DisplayInfo()