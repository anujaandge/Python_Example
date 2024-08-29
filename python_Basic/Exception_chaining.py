try:
    file=open("Example.txt")
except OSError:
    raise FileNotFoundError("unable to open file") 


#raise from statement
try:
    open("nofile.txt")
except OSError as exc:
    raise RuntimeError from exc    
    
    
#raise from None statement
try:
    open("nofile.txt")
except OSError as exc:
    raise RuntimeError from None
            