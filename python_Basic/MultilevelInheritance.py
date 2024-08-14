class GrandFather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
        
        
class Father(GrandFather):
    def __init__(self, fathername, grandfathername):
        GrandFather.__init__(self, grandfathername)
        self.fathername=fathername        
        
class Son(Father):
    def __init__(self,name, fathername, grandfathername):
        self.name=name
        Father.__init__(self, fathername, grandfathername)    
        
    def Print(self):
        print("son name ",self.name)
        print("Father name ",self.fathername)
        print("GrandFather name ",self.grandfathername)        
        
s=Son("Atharv","Anil", "Tukaram")
s.Print()        