try:
    num=int(input("Enter a number"))
    result=10/num
    print(f"Result={result}")
except ZeroDivisionError as e:
    print("Error:Can not divivde bye zero")    
    
except ValueError as e:
    print("Error:Please enter a valid number")    