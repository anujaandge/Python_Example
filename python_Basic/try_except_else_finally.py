try:
    s=input("Enter a file name: ")
    file=open(s, "r")
    content=file.read()
    print(content)

except FileNotFoundError as e:
    print("Error: The file was not found")
    
else:
    print("file read operation sucessful..")

finally:
    if 'file' in locals():
       file.close()
    print("file operation is completed..")                