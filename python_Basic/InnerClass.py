class Student:
    def __init__(self):
        self.name= "Anu"
        self.subject=self.Subjects()
        pass
    
    def show(self):
        print("Name:", self.name)
        self.subject.display()
    class Subjects:
        def __init__(self):
            self.sub1= "phy"
            self.sub2= "math"
            
        def display(self):
            print("subject: ",self.sub1, self.sub2)    
            
s=Student()
s.show()            