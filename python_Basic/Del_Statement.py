a=[2,3,4,5,6,7]
del a[0]
print(a)
del a[3]
print(a)
del a[1:3]
print(a)
del a[:]
print(a)

del a

#Tuple & Ssequences
t='Anu','Nitin',1,2,345,'Hello'
print(t[0])
print(t)
u=t,(6,7,8,9)
print(u)
#t[0]=0
print(t)


#set
#sets are immutable 
#don't have indexing
s={'apple','orange','apple','pear','banana'}
print(s)
print('Orange'.lower() in s)
a=set('abracadabra')
print(a)  #unique letters in a
b=set('aldfahe')
print(b)   #unique letters in b
print(a-b) # letters in a but not in b
print(b-a) # letters in b but not in a
print(a|b) #letters in a or b or both
print(a&b) #letters in a and b both
print(a^b) #letters in a or b but not both

x={i for i in 'abcdjdmse' if i not in 'abc'}
print(x)

#Dictionaries
#has key value pair
#key are unique

tel={'Anu':24,'Nitin':29}
print(tel['Anu'])
print(tel)
tel['Sonal']=26
print(tel)
print(list(tel))
print(sorted(tel))
print('Nitin' in tel)
print('sonu' in tel)
n=dict([('space',34),('gaf',44),('dhf',583)])
print(n)
d={x:x**2 for x in (2,4,6)}
print(d)

