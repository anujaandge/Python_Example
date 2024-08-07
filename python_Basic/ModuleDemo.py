import fibonaciiSeries as fib
fib.fib(40)

#importing specific names from module, not including module
from fibonaciiSeries import fib
fib(50)
#importing all modules
from fibonaciiSeries import *
fib(60)

import sys
print(dir(fib)) # used to find out which names a module defines
print(dir()) #lists the names you have defined currently
print(dir(__builtins__)) # lists names of buil-in functions and variables





