# Variables & data types

# int
a = 1
print(type(a))

# float
b = 3.5
print(type(b))

# string
c = "myString"
print(type(c))

# list
my_list = ["A", "B", "C", "D"]
print(type(my_list))
print(my_list)
print(my_list[1])

my_list[1] = 7
print(my_list[1])

# tuple
my_tuple = ("A", "B", "C", "D")
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])

# my_tuple[1] = 7  # Will raise an error

# set
my_set = {1, 2, 3, 4}
print(type(my_set))
print(my_set)
# print(my_set[1])  # Will raise an error

for val in my_set:
    print(val)

# dict
my_dict = {"1": "first", "2": "secound", "3": "third"}
print(type(my_dict))
print(my_dict)

dict_values = my_dict.values()
print(dict_values)
print(type(dict_values))  # Type will be a class

print(my_dict["1"])
# print(my_dict["5"])  # Will raise an error

print(my_dict.get("1"))
print(my_dict.get("5"))  # Will return default value: None - if key doesn't exists
print(my_dict.get("5", "Banana"))  # Will return custom value: Banana - if key doesn't exists

# Flow control
a = 1
b = 5

# If, Else
if a < b:
    print("A is smaller")
else:
    if a > b:
        print("B is smaller")
    else:
        print("A = B")

a = 5
b = 2

# Elif
if a < b:
    print("A is smaller")
elif a > b:
    print("B is smaller")
else:
    print("A = B")

# For, while
my_list = [1, 2, 3, 4, 5]

print("\nWhile")
i = 1
while i <= len(my_list):
    print(i)
    i += 1

print("\nFor")
for elem in my_list:
    print(elem)

# Continue
print("\nContinue")
for elem in my_list:
    if elem == 3:
        continue  # Will skip if elem == 3
    print(elem)

print("\nBreak")
for elem in my_list:
    if elem == 3:
        break  # Will stop execution if elem == 3
    print(elem)

print("\nPass")
for elem in my_list:
    if elem == 3:
        pass  # Will do nothing
    else:
        print(elem)

a = 10
if a > 5:
    pass  # Will do nothing
