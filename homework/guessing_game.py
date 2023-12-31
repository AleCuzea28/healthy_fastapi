# 2. Guessing game: The user should guess a random number between 10000 and 99999. 
# Use python built-in function `input` to get the user's number. 
# Compare the 2 numbers and tell the user how many digits he got right. 
# Do not tell him which ones. Play the game until the user guesses. 
# Or until he rage quits.

from random import randint


def compare_numbers(first, second):
    
    guessed_digits = 0
    first_list = [int(x) for x in str(first)]
    second_list = [int(x) for x in str(second)]
    for i in range(len(first_list)):
        if first_list[i] == second_list[i]:
            guessed_digits += 1

    return guessed_digits        


def guessing_number():

    while True:
        print("Please choose a number between 10000 and 99999. ")
        user_choice: int = int(input("Your guess:"))
        if user_choice == random_number:
            print("Congrats! You have guessed")
        else:
            print(f"You have guessed {compare_numbers(random_number,user_choice)} digits! ")
            print("Try again! :)")


if __name__ == '__main__':

    random_number = randint(10000,99999)
    print(random_number)

    print("Welcome to guessing game!")
    guessing_number()
