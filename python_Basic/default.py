def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
#ask_ok('Do you really want to quit')
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
#parrot(1000) 
#parrot(voltage=2000)
#parrot(voltage=1000,action='Vooom')   
#parrot('a million','bereft of life','jump')        

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        

#cheeseshop("Limburger", "It's very runny, sir", "It's really very, VERY runny, sir.",shopkeeper="Michael Palin", client="John Cleese",sketch="Cheese Shop Sketch")


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg,/):
    print(arg)
def kwd_only_arg(*,arg):
    print(arg)
def combined_example(pos_only,/,standard,*,kwd_only):
    print(pos_only,standard,kwd_only)    
standard_arg(1)
standard_arg(2)      
standard_arg(arg=3)  
pos_only_arg(4)
#pos_only_arg(arg=5) throws error only take value with position
# kwd_only_arg(5) throws erro only yake value with keyword 
kwd_only_arg(arg=5) 

#combined_example(6,7,8) error
combined_example(6,7,kwd_only=8)

def concat(*args,sep=" + "):
    print(sep.join(args))
concat('Anuja','Nitin','Gore')    

args=[3,7]
print(list(range(*args)))
#lambda expression

def make_increment(n):
    return lambda x:x+n
f=make_increment(42)
print(f(0))
print(f(4))

        