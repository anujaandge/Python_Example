#Built in library function
#user defined functions

def fun(): #creating a function
    print("My name is Anuja")

fun()#calling a function    

#function with parameters
def add(num1:int, num2: int) ->int:
    num3=num1+num2
    return num3
num1, num2= 5,12
ans=add(num1, num2)
print(f"The addition of {num1} and {num2} is {ans}.")


#Types of function Arguments
#1.Default arguments

def myFun(x, y=10): #default argument y
    print("x: ",x)
    print("y: ",y)
    
myFun(23)
myFun(12,23)    

#2.Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
    
    
student(firstname="Anuja", lastname="Andge")
student(lastname="Andge", firstname="Anuja")
  
#3.Positional Arguments
def nameAge(name, age):
    print('Hi, I am ',name)
    print("My age is ",age)
print("case1")
nameAge("Anuja", 23)
print("case2")
nameAge(23,"Anuja")    

#4.Arbitrary Keyword Argumnets
# *args -non-keyword argument

def demo(*args):
    for arg in args:
        print(arg)
demo("Hello","Welcome","to","Gfg")        

# **kwargs -keyword arguments
def demo2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))
demo2(first="one",second="Two",Third="Three")        
        
#Anonymous Function
#lambda keyword is used to create Anonymous function
def cube(x):return x*x*x

cube_v=lambda x:x*x*x  #anonymous function
print(cube(3))
print(cube_v(4))        

#Recursive function
#Example:factorial of number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(4))    