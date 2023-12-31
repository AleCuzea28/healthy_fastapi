# Classes
class MyClass:
    def my_function(self):
        print("Hello")

    def param_function(self, number: int):
        print(f"Your number is {number}")


my_obj = MyClass()
my_obj.my_function()
my_obj.param_function(5)


# Custom Exception
class MyException(Exception):  # Extends Exception class
    var1 = "Class variable"

    def __init__(self, message, *args):  # Constructor
        self.message = message

    def __str__(self):  # String representation of the class
        return f"My class: Message: {self.message}, Var: {self.var1}"


# Raise a custom exception
a = 1
if a == 1:
    raise MyException("Mesaj")
