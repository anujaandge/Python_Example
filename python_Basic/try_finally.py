try:
    file=open("Example.txt","w")
    file.write("This is my test file")
    
finally:
    print("Error: can't find the file")    