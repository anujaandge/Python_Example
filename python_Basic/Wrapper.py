class SimpleClass:
    def __init__(self, value):
        self.value = value
        
    def double(self):
        return self.value * 2
    
class WrapperClass:
    def __init__(self, wrapped_class):
        self._wrappedd_class= wrapped_class
        
    def double(self):
        print(f"calling double method with value:{self._wrappedd_class.value}")
        result=self._wrappedd_class.double()
        print(f"result:{result}")
        
simpObj=SimpleClass(5)

wrapObj=WrapperClass(simpObj)
wrapObj.double()            
                
    