def my_decorator(func):
    def wrapper():
        print("Something before....")
        func()
        print("Something after.....")
    return wrapper

def do_twice(func):
    def wrapper_do_twice():
        print("Do twice")
        func()
        func()
    return wrapper_do_twice
   

def do_twice_with_any_args(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

