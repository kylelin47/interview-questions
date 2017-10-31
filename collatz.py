"""
Imagine a function that obeys the following rules:

Given a positive integer,
    * If the number is one, stop
    * If the number is even, divide it by two
    * If the number is odd, triple it and add one

1. Write a method that takes in a positive integer and returns the sequence that results from continually applying this function, taking the result at each step as the input to the next.

For example,

f(12) would return [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]


Consider:
    * Does this sequence end? (Assume that it does)
    * Overflows (stack, integer)
    * Can the sequence be too long to store in memory? (Assume that it can be)
"""

# Just assume that it's a positive integer coming in.

# Recursively - hopefully you don't do it this way. Consider stack overflow
def recursive(n):
    sequence = []
    __recursive(n, sequence)
    return sequence

def __recursive(n, sequence):
    sequence.append(int(n))
    if n == 1:
        return
    if n % 2 == 0:
        __recursive(n/2, sequence)
    else:
        __recursive(n*3 + 1, sequence)

# Iteratively
def iterative(n):
    sequence = []
    while not n == 1:
        sequence.append(int(n))
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
    sequence.append(1)
    return sequence

# Generators if you're feeling spicy and working in Python
def generator(n):
    return [val for val in __generator(n)]

def __generator(n):
    while not n == 1:
        yield int(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
    yield 1
