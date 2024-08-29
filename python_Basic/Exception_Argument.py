#argument gives additional information about the problem
def print_number(str):
    try:
        return(int(str))
    except ValueError as Arugument:
        print("The argument does not contain number",Arugument)
        
print_number("Abc")        