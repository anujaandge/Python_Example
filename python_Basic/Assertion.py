# #assertion
# num=int(input("Enter the number: "))
# assert num>=0 and num<=100
# print("number is ",num)

# #custom assertion
# num=int(input("Enter the number: "))
# assert num>=0 and num<=100, "number should be in between 0 to 100"
# print("number is ",num)

#Handling Assertion
try:
    num=int(input("Enter the number: "))
    assert num>=0 and num<=100, "number should be in between 0 to 100"
    print("number is ",num)
except AssertionError as msg:
    print(msg)    