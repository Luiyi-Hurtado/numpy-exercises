#!/usr/bin/python3
"""
Function to test whether any of the elements
of a given is non-zero
"""


import numpy as np


def main():
    """
    Determinate if the array have a zero in
    a elements from a array using any function

    Args:
        Nothing

    Returns:
        new boolean or ndarray is returned unless
        out is specified, in which case a reference
        to out is returned.
    """
    arr1 = np.array([0, 0, 0, 0])
    arr2 = np.array([1, 2, 3, 4])

    print(arr1)
    print(np.any(arr1))
    print(arr2)
    print(np.any(arr2))


if __name__ == "__main__":
    main()
