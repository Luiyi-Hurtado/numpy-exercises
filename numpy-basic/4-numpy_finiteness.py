#!/usr/bin/python3
"""
Function to test a given array element-wise
for finiteness
"""


import numpy as np


def main():
    """
    Determinete for the array have a finite
    element with the isfinite() function

    Args:
        Nothing

    Returns:
        ndarray or boolean:
            True where arrays is not postive or negative
            infinite, or NaN; False otherwise
    """
    arr1 = np.array([np.inf, 1, np.nan, -0])
    print(arr1)
    print(np.isfinite(arr1))


if __name__ == "__main__":
    main()
