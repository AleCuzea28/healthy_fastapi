import os

# file = open("exemplu.txt", "w")
# file.write("Hello, World!")
# file.close()

# with open("exemplu2.txt", "w") as file:
#     file.write("Hola")


def read_file(filename):
    with open(filename, "r") as file2:
        data = file2.read()
        print(data)
#
# print(data)

def get_first_line_of_file():
    with open("exemplu2.txt", "r") as file3:
        data = file3.readline()
        print(data)

def get_first_line_of_file_2():
    with open("exemplu2.txt", "r") as file3:
        data = file3.readline()
        print(data[0])

# what happens if an error occurs during write? the file is never closed.
# you basically have 2 options: either use try except or use with

# def read_file(filename):
#     with open(filename, "r") as file:
#         file.read()


# read_file("exemplu.txt")


# def write_file(filename):
#     with open(filename, "w") as file:
#         data = "a string"
#         file.write(data)
#
#
def write_with_append(filename):
    with open(filename, "a") as file:
        data = "we append this text"
        file.write(data)


# write_with_append("exemplu2.txt")
# read_file("exemplu2.txt")

# basepath = '/Users/alexandraveres/work/syneto-lab-dark-side/'
# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_dir():
#             print(entry.name)

import json

with open("lab4.json") as json_file:
    content = json_file.read()
    print(json.loads(content))

my_dict = {"jan": 1, "feb": 2}

my_js = json.dumps(my_dict)

with open("example.json", "w") as json_file2:
    json_file2.write(my_js)