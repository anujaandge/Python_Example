class Employee:
    #name="Anu"
    #age=23
    empCount=0 #class attribute
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        #modifying class attributes
        
        Employee.empCount+=1
        print("Name: ",self.__name, ", Age: ",self.__age)
        print("Employee Count:",Employee.empCount)
    
emp=Employee("Anu",23)
#print("name: ",emp.name) #accessing class attributes
#print("age: ",emp.age)
print()
e1=Employee("Nitin",28)

    