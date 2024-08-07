#formating string literals method
fname="Anuja"
lname="Gore"
print(f"My name is {fname} {lname}")
print(F"My name is {fname} {lname}")

import math
print(f"the value of pi is {math.pi:.2f}")

table={'Anu':24,'Nitin':209,'Sonal':26}
for name,age in table.items():
    print(f'{name:8} ---{age:8d}')
    
animal='eels'
print(f"my house is full of {animal}")
print(f"my house is full of {animal!r}")
print(f"my house is full of {animal!s}")
print(f"my house is full of {animal!a}")

print(f"{fname=} {lname=}")

#str.format()
yes_votes=42_572_654
total_votes=85_705_149
prcentage=yes_votes / total_votes
print('{:9} YES votes {:2.2%}'.format(yes_votes, prcentage))

print('{0} and {1}'.format('spam','eggs'))
print('{1} and {0}'.format('spam','eggs'))
print('Anu:{0[Anu]:d}; Nitin:{0[Nitin]:d}; Sonal:{0[Sonal]:d}'.format(table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# namual formating of tabel
#str.rjust(),str.ljust(),str.center()
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
    
#str()
s="Hello, WOrld"
print(str(s))
a=str(1/7)
print(type(a))
#repr()
print(repr(s))
x=10*3.25
y=200*200
print('the value od x '+repr(x)+',and y is '+repr(y))


