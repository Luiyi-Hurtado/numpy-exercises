#!/usr/bin/python3
"""
Fucntion to test whether none of the elements
of a given array is zero
"""


import numpy as np


def main():
    """
    This function determinate elements of
    a given array is zero

    Args:
        Nothing

    Return:
        A new boolean or array is returned unless out is specified,
        in which case a reference to out is returned.
    """
    array1 = np.array([2, 1, 6])
    array2 = np.array([0, 1, 6])

    print(array1)
    print(np.all(array1))
    print(array2)
    print(np.all(array2))


if __name__ == "__main__":
    main()
