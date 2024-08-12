# while True:
#     try:
#         a=int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("That was no valid number ..Try again....")
        
        
        
# class A(Exception):
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# for cls in [A,B,C]:
#     try:
#         raise cls()
#     except C:
#         print("C")
#     except B:
#         print("B")         
#     except A:
#         print("A")   
        
# try:
#     raise Exception('spam','eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst) 
#     print(inst.args)
    
#     x,y=inst.args
#     print('x= ',x)
#     print('y= ',y)       
    
# import sys
# try:
#     f=open("Hello.txt")
#     s=f.readline()
#     i=int(s.strip())
# except OSError as err:
#     print("OS error: ",err)
# except ValueError:
#     print("could not convert data to an integer.")
# except Exception as err:
#     print(f"unexpected {err=},{type(err)=}")
#     raise                

       
# def divide_zero():
#     x=1/0
# try:
#     divide_zero()
# except ZeroDivisionError as e:
#     print(e)            
    
# #Raising Exceptions
# try:
#     raise NameError("HiThere")
# except NameError:
#     print('An exception flew by!')
#     raise

#Exception chaining
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
  