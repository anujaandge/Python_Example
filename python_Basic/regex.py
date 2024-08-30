#Raw string
normal="Hello\nWorld"
print(normal)
raw=r"Hello\nWorld"
print(raw)

#re.match()
import re
line="cats are smarter than dogs"
matobj=re.match(r"cats",line)
print("matobj.group():",matobj.group())
print(matobj.start(),matobj.end())
#matobj1=re.match(r"dogs",line)
#print(matobj1.group())

#re.search()
serchobj=re.search(r"dogs",line)
print("serchobj.group()",serchobj.group())
print(serchobj.start(),serchobj.end())

#re.findall()
string="simple is better than complex."
obj=re.findall(r"ple",string)
print(obj)
obj1=re.findall(r"\w*", string)
print(obj1)

#re.sub()
s="simple is better than complex. The lion is very dangerous. It is amzaing"
obj2=re.sub(r"is", r"was",s)
print(obj2)
obj3=re.sub(r"is", r"was", s, 2)  #it will replace only two positions
print(obj3)

#re.compile()
pattern=re.compile(r"is")
obj4=pattern.sub(r"was", string)
print(obj4)