# 3. Letters: Put a big text in a file (at least 100 lines). 
# Read the file and count each letter how many times it appears, case-insensitive.

import string

letters: dict = dict.fromkeys(string.ascii_lowercase, 0)

with open ("big_file_for_letters.txt", encoding="utf8") as file:
    data = file.read()
    for character in data:
        if character.lower() in letters.keys():
            letters[character.lower()] += 1

print(letters)

