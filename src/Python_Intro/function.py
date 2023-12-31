# Functions
def my_function(param: int) -> int:
    if type(param) is str:  # The is keyword is used to test if two variables refer to the same object
        pass
    else:
        print(type(param))
        print(param)
        return param


a = my_function("Hello")
b = my_function(5)

print(f"Value a: {a}")  # fstring: > python3.6 -  string formatting mechanism
print(f"Value b: {b}")

my_list = [1, 2, 3, 4]


def exception_handling(my_list):
    try:
        print(my_list[4])
    except IndexError:  # This happens first
        print("Index")
    except Exception:
        print("Exception")


def exception_handling_2(my_list):
    try:
        print(my_list[4])
    except Exception:  # This happens first
        print("Exception")
    except IndexError:
        print("Index")


exception_handling(my_list)
exception_handling_2(my_list)


# def exception_handling_3(my_list):
#     for elem in my_list:
#         if elem == 3:
#             raise Exception  # Breaks the execution

# exception_handling_3(my_list)

def exception_handling_3_with_try_except(my_list):
    try:
        for elem in my_list:
            if elem == 3:
                raise IndexError
    except IndexError:
        print("Index error raised my me :)")


exception_handling_3_with_try_except(my_list)
