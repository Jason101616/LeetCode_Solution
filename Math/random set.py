# generate a set of m integers from an array of size n.

import random


def pickMRecursively(original, m, i):
    if i + 1 == m:
        return original[:m]
    elif i + 1 > m:
        subset = pickMRecursively(original, m, i - 1)
        k = random.randint(0, i)
        if k < m:
            subset[k] = original[i]
        return subset
    return None


def pickMIteratively(original, m):
    subset = original[:m]
    for i in range(m, len(original)):
        k = random.randint(0, i)
        if k < m:
            subset[k] = original[i]
    return subset
