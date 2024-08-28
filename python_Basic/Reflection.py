#type() function


from typing import Any


print(type("Hello"))
print(type([1,2,3]))
#isinsatance()
print(isinstance(int, object))
print(isinstance(10, int))
print(isinstance("Hello", str))

#issubclass()
class Test:
    pass
print(issubclass(int, object))  
print(issubclass(str, object))
print(issubclass(Test, object))

#Callable ()
print(callable("Hello")) #false
print(callable(abs))
print(callable(list.clear([1,2,3]))) #false

class Test1:
    def __init__(self):
        self.name="Anuja"
    def __call__(self):
        print("Hello")
obj=Test1()        
print(callable(Test1))         #True

#getattr()
print(getattr(obj, "name")) #Anuja

#setattr()
setattr(obj,"age", 20)
setattr(obj, "name", "Nitin")
print(obj.name, obj.age)

#hasattr()
print(hasattr(obj, "age")) #true
print(hasattr(obj, "address")) #false

#dir()

print("dir(int): ", dir(int))
print("dir(str): ",dir(str))
print("dir(obj): ", dir(obj))
