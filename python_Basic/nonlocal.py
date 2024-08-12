# name='geek'
# def foo():
#     name='Geek'
#     def bar():
#         nonlocal name
#         print(name)
#         name='GEEK'
#         print(name)
        
#     bar()
#     print(name)
    
# foo()
# print(name)        

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
print(var1)    