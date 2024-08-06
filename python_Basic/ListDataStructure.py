a=[]
a.append(3) #[3]

b=[4,5,6]
a.extend(b)
print(a) #[3,4,5,6]

a.insert(1,2)
print(a) #[3,2,4,5,6]
a.insert(0,1)
print(a)  #[1,3,2,4,5,6]

a.remove(3) #[1,2,4,5,6]
a.insert(2,3)
print(a) #[1,2,3,4,5,6]

a.pop(-1)
print(a) #[1,2,3,4,5]

a=[1,2,3,4,5,2,2,2,2]
print(a.count(2))

a.reverse()
print(a)#2, 2, 2, 2, 5, 4, 3, 2, 1]

c=a.copy()
print(c)

a.sort()
print(a)

a.clear()
print(a)

print('\n')
print('-'*40)
print('\n')

#list as a stack
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack) #[3,4,5,6,7]

print(stack.pop()) #7
print('-'*40)

#using list as queues
from collections import deque
queue=deque(['Anu','Nitin','Sujata','Sonal'])
queue.appendleft('Vedant')
queue.append('Vivek')
print(queue)
queue.popleft()
print(queue)
print('-'*40)

#listComprehensions
#traditinal way
squ=[]
for i in range(10):
    squ.append(i**2)
print(squ)
#using listComprehensions    
squares=list(map(lambda x:x**2, range(10)))
print(squares)
square=[x**2 for x in range(10)]
print(square)

print('-'*40)

