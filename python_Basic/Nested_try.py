#example 1
a=10
b=0
# try:
#     print("From outer try block...")
#     print(a/b)
#     try:
#         print("This is inner try..")
#         #print(a/b)
#     except Exception:
#         print("General Exception.. ")
#     finally:
#         print("Inside inner finally block")
# except ZeroDivisionError:
#     print("can not divide by 0")
# finally:
#     print("Inside outer finally block..")            
                
        
#example 2
# try:
#     print("From outer try block...")
#     try:
#         print("This is inner try..")
#         print(a/b)
#     except ZeroDivisionError:
#         print("can not divide by 0")    
#     finally:
#         print("Inside inner finally block")
# except Exception:
#         print("General Exception.. ")
# finally:
#     print("Inside outer finally block..")            
    
#example 3
try:
    print("From outer try block...")
    try:
        print("This is inner try..")
        print(a/b)
    except KeyError:
        print("Key Error")    
    finally:
        print("Inside inner finally block")
except ZeroDivisionError:
        print("Can not divide by 0 ")
finally:
    print("Inside outer finally block..")                