tup=("c",'d','a','a','b','b','a')

print(tup.count('a'))

li=["c",'d','a','a','b','b','a']
print(li)
li.sort()
print(li)

dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}

print(dict)
s={'python','java','c++','python','javascript','java','python','java','c++','c'}
print(len(s))


dict1={}
for i in range(3):
    name=input("enter subject name: ")
    marks=input("enter marks: ")
    dict1[name]=int(marks)
    
print(dict1)    