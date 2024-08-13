def scope_test():
    def do_local():
        spam="local spam"
    def do_nonlocal():
        nonlocal spam
        #print(spam)
        spam="nonlocal spam"    
    def do_glbal():
        global spam
        
        spam="global spam"  
       # print(spam)  
        
    spam='test spam'
    do_local()
    print('Afetr local assignment: ',spam)
    do_nonlocal()
    print("After nonlocal assignment: ",spam) 
    do_glbal()
    print("After gloabal assignmnet: ",spam)
    
scope_test()
print("global scope: ",spam)       