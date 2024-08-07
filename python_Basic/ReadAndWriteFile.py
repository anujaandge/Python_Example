# mode r -on;u read the file
#w-only write
#a-opens for appending
#b-opens file in binary mode
#r+ -for both read and write


# with open('Hello.txt',encoding="utf-8") as f:
#     read_data=f.read() #we can also use f.readlines()
#     #read_line=f.readline()
    
# print(read_data)  
# #print(read_line)  
# print(f.closed)

s=open('Hello.txt','r+',encoding="utf-8")
print(s.readline())
s.write('\nTesting..')
value=('my age',24)
a=str(value)
s.write('\n'+a)
