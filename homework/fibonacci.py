# 1. Fibonacci: Create a function which generates the Fibonacci sequence.
# The function has one parameter which specifies how many numbers should be generated.
# Return the generated sequence.

from typing import List


def fib_sequence(how_many_number_to_generate: int) -> List[int]:
    my_fib_sequence: List[int] = [0]
    if how_many_number_to_generate == 2:
        my_fib_sequence.append(1)
    elif how_many_number_to_generate == 1:
        pass
    else:
        my_fib_sequence.append(1)
        for i in range(3, how_many_number_to_generate + 1):
            fib = my_fib_sequence[i - 2] + my_fib_sequence[i - 3]
            my_fib_sequence.append(fib)
    return my_fib_sequence


if __name__ == "__main__":
    print(fib_sequence(6))
