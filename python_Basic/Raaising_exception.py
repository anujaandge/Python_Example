def div(a,b):
    if b==0:
        raise ZeroDivisionError("cannot divide by zero")
    return (a/b)

try:
    a=int(input("Enter a: "))
    b=int(input("Enter b; "))
    result=div(a, b)
    
except ZeroDivisionError as e:
    print(e)
    
else:
    print(result)        