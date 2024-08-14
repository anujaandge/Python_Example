class Student:
    def __init__(self,name ,profetion):
        self.sname=name
        self.sprofetion=profetion
    
        print(f"My name is {self.sname} & my profetion is {self.sprofetion}")    

class Inten:
    def __init__(self,name,profetion) -> None:
         self.iname=name
         self.iprofetion=profetion       
         print(f"My name is {self.iname} & my profetion is {self.iprofetion}")
         
class Person(Student, Inten):
    def __init__(self, name, profetion):
        self.name=name
        self.profetion=profetion
        Student.__init__(self,name, "student")
        Inten.__init__(self,name,"Intern")       

p=Person("Anu","student")        
              