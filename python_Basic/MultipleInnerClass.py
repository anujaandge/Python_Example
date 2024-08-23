#This is an example of multiple inner classs
class organization:
    def __init__(self):
        self.dept1= self.Department1()
        self.dept2= self.Department2()
    
    def show(self):
        print("Welcome to our organization")
        
    class Department1:
        def display_department1(self):
            print("Indepartment 1")
            
    class Department2:
        def display_departmet2(self):
            print("In department 2")
            
            
obj=organization()     
obj.show()
dept1=obj.dept1
dept1.display_department1()
dept2=obj.dept2
dept2.display_departmet2()                 
        