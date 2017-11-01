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
    * Input validation (Assume that inputs to this and subsequent questions are valid)
"""

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
        __recursive(n / 2, sequence)
    else:
        __recursive(n * 3 + 1, sequence)

# Iteratively


def iterative(n):
    sequence = []
    while not n == 1:
        sequence.append(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    sequence.append(1)
    return sequence

# Generators if you're feeling spicy and working in Python


def generator(n):
    return [val for val in __generator(n)]


def __generator(n):
    while not n == 1:
        yield int(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    yield 1


"""
Maybe not do this one as it's very similar to Project Euler #14.
2. Given a range [start, end] of positive integers, return the integer in that range that has the longest sequence generated before it stops, using the rules from #1.

Consider:
    * Ties. Just say any of them is a valid answer. Or prove that there will only be one
"""

"""
Naive implementation

Problem - inefficient. Why?
    * Recalculations of sequence lengths for numbers you've already seen.
    * Values less than end/2 cannot possibly generate the longest sequence.
    * Reuse of methods created in step 1 means you're generating a lot of lists, but you don't actually care about the numbers in the sequence, just the length
"""


def longest_sequence(start, end):
    max_length = [start, 0]
    for i in range(start, end + 1):
        length = len(generator(i))
        if length > max_length[1]:
            max_length = [i, length]
    return max_length[0]


# The max(start, end/2) is always helpful. Whether it's helpful to cache is somewhat dependent on the range of [start, end], but mostly a good idea


def longest_sequence_end_divided(start, end):
    max_length = [start, 0]
    for i in range(max(start, int(end / 2)), end + 1):
        length = sequence_length(i)
        if length > max_length[1]:
            max_length = (i, length)
    return max_length[0]


def sequence_length(n):
    length = 1
    while not n == 1:
        if n % 2 == 0:
            length += 1
            n = n / 2
        else:
            length += 2
            n = (n * 3 + 1) / 2
    return length

# Not the most efficient way of caching for this problem, but hey


def longest_sequence_cached(start, end):
    max_length = [start, 0]
    seen = {}
    for i in range(max(start, int(end / 2)), end + 1):
        length = sequence_length_cached(i, seen)
        seen[i] = length
        if length > max_length[1]:
            max_length = [i, length]
    return max_length[0]


def sequence_length_cached(n, cache):
    length = 1
    while not n == 1:
        if n in cache:
            return cache[n] + length
        if n % 2 == 0:
            length += 1
            n = n / 2
        else:
            length += 2
            n = (n * 3 + 1) / 2
    return length

"""
Maybe use this one instead of #2
3. I have a range [start, end] of positive integers. Using the rules from #1, I generate all sequences that start with one of the integers in the range.
I look through the sequences and I compute which integer /that is also in the range/ appears the most

Given this range, how can you determine my value?

Consider:
    * Multiple right answers. Return any
    * First instinct may be to use a map to track how often you've seen a value in the past. However, integers in the sequence which are outside of the range are completely unimportant.
      Thus, if you were to use a map, your keyspace would be defined as [start, end] or smaller; maybe it would be better to just use an array.
    * 1 is guaranteed to be the most common if it's in the range, followed by 2. In general, powers of two are more common. Probably don't actually use this information.
    * If a range contains both n and n * 2, n * 2 is guaranteed to not be the correct answer.
"""

# Most straight-forward.

from collections import defaultdict


def most_common(start, end):
    seen_values_count = defaultdict(int)
    for i in range(start, end + 1):
        sequence = generator(i)
        for val in sequence:
            if val >= start and val <= end:
                seen_values_count[val] += 1
    return max(seen_values_count, key=lambda k: seen_values_count[k])

"""
4. Imagine you were trying to solve #3, but were given a large range of values, such that it's prohibitively expensive on a single machine.
How might you design a system to split the work amongst many?

Consider:
    * Equal distribution of work. How would you divide the range among the machines?
    * What does each machine need to figure out, to guarantee a correct final output?
"""
