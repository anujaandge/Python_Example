# class Parent:
#     def myMethod(self):
#         print("calling parent method")
        
                                    
# class Child(Parent):
#     def myMethod(self):
#         print("calling child method")
        
# c=Child()
# c.myMethod()        

#2nd Example
class Employee:
    def __init__(self,name, salary):
        self.name= name
        self.salary= salary
    
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary
    
class SalesOfficer(Employee):
    def __init__(self, name, salary, incentive):
        super().__init__(name, salary)    
        self.incnt= incentive
        
    def getSalary(self):
        return self.salary+self.incnt
    
    
e1=Employee("Rajesh", 9000)
print(f"Total salay for {e1.getName()} is Rs {e1.getSalary()}")
s1=SalesOfficer("Kiran",10000,1000)
print(f"Total salary for {s1.getName()} is Rs {s1.getSalary()}")    
              