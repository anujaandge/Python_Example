#self parameter
# used in instance methods to refer to the instance itself
#Note:
# its pointer to Current object

class Mynumber:
    def __init__(self, value):  # self constructor
        self.value=value
    
    def print_value(self):
        print(self.value)
 
     
obj=Mynumber(23)
obj.print_value()            