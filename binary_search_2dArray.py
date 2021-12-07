import numpy as np


def binary_search(a_list, item):
    # A customized binary search algorithm for 2D Numpy arrays. Super fast.
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if np.array_equal(a_list[midpoint], item):
            found = True
            return midpoint
        else:
            if item[0][0] < a_list[midpoint][0][0]:
                last = midpoint - 1
            elif item[0][0] == a_list[midpoint][0][0]:
                rng = len(a_list) // 6
                for i in range(-rng, rng):
                    if np.array_equal(a_list[midpoint + i], item):
                        return midpoint+i
            else:
                first = midpoint + 1