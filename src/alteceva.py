from myDecorators import my_decorator, do_twice, do_twice_with_any_args

# from myDecorators import do_twice, do_twice_with_any_args

def say_hello():
    print("Mesaj")

# say_hello = my_decorator(say_hello)
# say_hello()    

@my_decorator
def say_wohoo():
    print("wohoo")

say_wohoo()

@do_twice
def say_whee():
    print("whee")

say_whee()    

@do_twice_with_any_args
def say_any(*args, **kwargs):
    for idx in args:
        print(idx)

    for key in kwargs.keys():
        print(key)    

say_any(2, 3, a=5, b=6)        

