i=1
while(i<=100):
    print(i)
    i+=1
print('--------------')
j=100
while(j>=1):
    print(j)
    j-=1    
    
print('--------------')  
n=int(input("Enter the value of n:")) 
for i in range(1,11):
    print(f'{n}*{i}=',n*i) 
    
print('--------------')
li=[1,4,9,16,25,36,49,64,81,100] 
for i in range(len(li)):
    print(li[i])   
    
print('--------------') 
x=int(input('Enter value to search:'))
for i in range(len(li)):
    if li[i]==x:
        print(f'{x} is present at index {i}')   