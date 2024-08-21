class Student:
    def __init__(self,name, grade): #instance attribute
        self.__name=name
        self.__grade=grade
        print("Name: ",self.__name," , grade: ",self.__grade)
        
s1=Student("Ram", "B")
s2=Student("Mayur", "A")        
