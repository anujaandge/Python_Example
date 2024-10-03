def str_upper(func):
    def inner():
        str=func()
        return str.upper()
    return inner 

def str_split(func):
    def inner():
        str=func()
        return str.split()
    return inner

@str_split
@str_upper #decorator is used to modify the function
def print_str():
    return "good morning"

print(print_str())