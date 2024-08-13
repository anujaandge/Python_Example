class Dog:
    str1="mammal"
    str2="Dog"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"My name is {self.name}") 
    def fun(self):
        print("I,m a ",self.str1)
        print("I'm a ",self.str2)      
    
    
Bruno=Dog("Bruno")
Tyson=Dog("Tyson")
print(f"Bruno is a {Bruno.__class__.str1}")
print(f"Tyson is not {Tyson.__class__.str1}")

# print(f"My name is {Bruno.name}")
# print(f"my name is {Tyson.name}")
Bruno.speak()
Tyson.speak()
print(Bruno.str1)
Bruno.fun()


    