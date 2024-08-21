class Student:
    stdCount = 0
    def __init__(self, name, age):
        self.__name= name
        self.__age= age
        Student.stdCount +=1
        
    #creating static method
    @staticmethod
    def showCount():
        print(Student.stdCount)
        
e1=Student("ssd", 23)
e2=Student("asw", 23)
e3=Student("xyz", 12)
Student.showCount()        
        