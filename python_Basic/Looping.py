dict={'Anu':24,'Nitin':29,'Sonal':26}
for k,v in dict.items(): #both key and value
    print(k, v)
for k in  dict.keys(): #only keys
    print(k)   
for v in dict.values(): #only values
    print(v)    
    
     
#enumerate() used to get index and value at the same time    
a=['apple','orange','banana']
for i,v in enumerate(a):
    print(i, v)
    
 #Zip() used to loop over two or more sequances at same time   
x=[2,4,6]
y=[4,16,36]
for i,j in zip(x,y):
    print(i,j) 
    
#reversed() used to loop over sequence in reverse
for i in reversed(range(1,10,2)):
    print(i)

#sorted()  used for sorting the list
for i in sorted(a):
    print(i)
#set() removes duplicate
a=['apple','orange','banana','apple','apple']
for i in sorted(set(a)):
    print(i)    
    
    
import fibonaciiSeries
fibonaciiSeries.fib(100)    
    
             