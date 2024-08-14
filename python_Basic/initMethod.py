class person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello, my name is ",self.name)
        
p1=person("Anuja")
p2=person("Nitin")
p3=person("Sonal")
p1.say_hi()
p2.say_hi()
p3.say_hi()   


#__init__ method with inheritance

class A(object):
    def __init__(self,name):
        print("A init called")
        self.name=name
        print(self.name)
        
class B(A):
    def __init__(self, name):
        print("B init called")  
        #a=A("ghj")  
        super().__init__(name='Ni')   
        A("saa") 
       # print("B init called") 
        self.name=name
        print(self.name)   
        
obj=B("anujas")  
obj.__init__("daj")      
B.__init__(B, name="gsj")