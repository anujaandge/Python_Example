try:
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    div= a/b
except ZeroDivisionError as e:
    print("Error can not divide by zero..")
    
except ValueError as e:
    print("Error: Please enter valid numbers..")

else:
    print(f"Division={div}")            