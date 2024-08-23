# @property is ued to use method as property
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math =math
        
    @property
    def percentage(self):
        return str((self.phy+ self.chem+ self.math)/3)+"%"
    
s=Student(98, 90, 89)
print(s.percentage)
s.phy=80
print(s.percentage)        