#What is a decorator?
# A decorator in Python is a function that takes another function as its argument, and returns yet another function . 
# Decorators can be extremely useful as they allow the extension of an existing function, without any modification 
# to the original function source code



def my_decorator(func):
    def wrap_func():
        print("*********")
        func()
        print("*********")
        
    return wrap_func

@my_decorator
def hello():
    print("helllllllo")

@my_decorator
def bye():
    print("See you later")

hello()
bye()
