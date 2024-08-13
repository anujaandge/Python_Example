#The nonlocal keyword is used in nested functions to 
# reference a variable in the parent function. 

#Advantage
#It helps in accessing the variable in the upper scope
#memeory added of variable is reused that saves memory

#Disadvantage
#can't used to referance global or local variables
#only be used inside nested structures


name='geek'
def method():
    def mod():
        #nonlocal name #compile time error occors
        print(name)
        name="Greek"


def foo():
    name='Geek'
    def bar():
        nonlocal name
        print(name)
        name='GEEK'
        print(name)
        
    bar()
    print(name)
    
foo()
print(name)        

def fun():
    var1=10
    def add():
        nonlocal var1
        print(var1)
        var1=var1+20
        print(var1)
    add()
    print(var1)
fun()    
   