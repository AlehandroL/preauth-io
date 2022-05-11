def firstSubset(M: list, N: int) -> [int, int] or None:
    complements = {}
    for m in M:
        complement = N - m
        if complements.get(complement) is not None: return [complement, m]
        complements[m] = complement
