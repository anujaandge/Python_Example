
def div_decor(func):
    def inner(*args):
        li=args[1:]
        try:
            for i in li:
                if i == 0:
                    raise ValueError("Division by zero is not allowed")
            return func(*args)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return inner        

@div_decor
def div1(a,b):
    return a/b

@div_decor
def div2(a,b,c):
    return a/b/c

print(div1(10,2))
print(div2(10,2,0))