#Let M be a not empty set of integer numbers, find the first subset of 2 numbers of M which sum N. For instance, let's say we've got a set of numbers [2, 5, 8, 14, 0] and N = 10, the resulting subset should be [2, 8].

#Challenge
#You're required to create a function that receives an array (M) and integer value (N). This function has to return an array of the first possible solution.


def firstSubset(M: list, N: int) -> [int, int] or None:
    complements = {}
    for m in M:
        complement = N - m
        if complements.get(complement) is not None: return [complement, m]
        complements[m] = complement
