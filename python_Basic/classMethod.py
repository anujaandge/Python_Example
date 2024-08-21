class Employee:
    empCount=0
    def __init__(self,name, age):
        self.name = name
        self.age = age
        Employee.empCount +=1
        
    @classmethod
    def showcount(cls):
        print(cls.empCount)
        
    @classmethod
    def newemployee(cls, name, age):
        return(cls(name, age))
    
e1=Employee("Bhavna", 24)
e2=Employee("Vivek", 12)
e3=Employee("Vedant",23)
e4=Employee.newemployee("Anil", 30)
Employee.showcount() 


#Dynamically add class Method to class
#use setattr() function

class Cloth:
    pass

@classmethod
def brandName(cls):
    print("Name of the brand is Rymond")
    
#adding dynamically
setattr(Cloth, "brand_name", brandName)
obj=Cloth()
obj.brand_name()    
           