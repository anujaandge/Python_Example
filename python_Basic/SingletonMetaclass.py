#creating singleton class by using meta class

class SingletonMeta(type):
    _instances={}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls]= super(SingletonMeta, cls).__call__(*args, **kwds)
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    pass

Singleton1=Singleton()
Singleton2=Singleton()
print(Singleton1==Singleton2)    