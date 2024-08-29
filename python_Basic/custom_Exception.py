class My_Exception(Exception):
    def __init__(self, age, message="The age must be in between 18 and 100"):
        self.age=age
        self.message=message
        super().__init__(self.message)
         
    def __str__(self):
        return  f"{self.message}.provide age:{self.age}"
    
def set_age(age):
    if age<18 or age>100:
        raise My_Exception(age)
    print(f"Age is set to {age}")

try:
    set_age(12)
except My_Exception as e:
    print(f"invalid age:{e.age}.{e.message}")             