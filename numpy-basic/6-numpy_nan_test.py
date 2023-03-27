#!/usr/bin/python3
"""
Fucntion to test element-wise for NaN of
a given array
"""


import numpy as np


def main():
    """
    Determinate if the elements of the array
    is a Nan, using isnan() function
    """
    arr = np.array([np.inf, np.nan, 1., -np.log(1)])
    print(arr)
    print(np.isnan(arr))


if __name__ == "__main__":
    main()
