from mydecorators import my_decorator, do_twice, do_twice_with_any_args


def say_hello():
    print("Hello! :)")


# say_hello = my_decorator(say_hello)
# say_hello()


@my_decorator
def say_wohoo():
    print("wohoo!")


# say_wohoo()
#
#
# say_wohoo()
#
@do_twice
def say_whee():
    print("Whee!!!!")


say_whee()

@do_twice_with_any_args
def say_any(*args, **kwargs):
    for idx in args:
        print(idx)

    for key in kwargs.keys():
        print(key)


# say_any(2, 3, a=5, b=6)

# abstract methods
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Hexagon(Square):

    def area(self):
        return self.side ** 3


square = Square(2)
print(square.area())
hexagon = Hexagon(2)
print(hexagon.area())