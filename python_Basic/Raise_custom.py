class my_exception(Exception):
    pass

def faulty_fun():
    raise my_exception("somthing went wrong in risky function..")

try:
    faulty_fun()
except my_exception as e:
    print(e)
        