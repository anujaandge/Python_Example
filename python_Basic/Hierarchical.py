class Parent:
    def func1(self) :
        print("This function is in parent")
        
class Child1(Parent):
    def func2(self):
        print("This function is in child 1")
        
class Child2(Parent):
    def fun3(self):
        print("This function is in child 2")
        
obj1=Child1()
obj1.func1()
obj1.func2()
obj2=Child2()
obj2.func1()
obj2.fun3()