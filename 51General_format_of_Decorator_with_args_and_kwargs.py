#This is the decorator pattern or general formate of decorator 

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args,**kwargs)
    return wrap_func

@my_decorator
def hello(greetings, emoji=":("):
    print(greetings,emoji)

hello("hiiiii")