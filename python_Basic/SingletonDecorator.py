#cretae singleton class using decorator
def Singleton(cls):
    instances={}
    def get_instance(*args, **kwargs):
        if cls not in instances:
             instances[cls]=cls( *args, **kwargs)
        return instances[cls]
    
    return get_instance     

@Singleton
class Signgleton:
    pass

s1=Signgleton()
s2=Signgleton()