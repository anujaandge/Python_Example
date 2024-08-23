#creating anonymous class
anonymous_class=type("Anoymous class", (), {'greet':lambda self:"Hello from anonymous class"})
#creting instance of anonymous class
obj=anonymous_class()
print(obj.greet())


#anonymous object
print(type("Hii"))

#lambda function
add=lambda x, y : x+y
print(add(3,4))