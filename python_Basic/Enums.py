#importing enum
from enum import Enum, unique
@unique
class Subject(Enum):
    English=1
    Maths=2
    Science=3
    Sanskrit=4
    
# obj=Subject.Maths
# print(type(obj))
# print(obj.name) #accessing enum name
# print(obj.value)    #accessing value


#Enum class is also used as constructor

department=Enum("Departments", "CSE IT ENTC ELECTRICAL ")
print(department.CSE)
print(department.IT)
print(department.ENTC)