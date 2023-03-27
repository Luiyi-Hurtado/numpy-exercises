#!/usr/bin/python3
"""
Function to test element-wise for positive
or negative infinity
"""


import numpy as np


def main():
    """
    Determinate if the array is a inf positive
    or negative

    Args:
        Nothing

    Returns
        A Traue value where array is inifinity positive or negative,
        False otherwise
    """
    arr = np.array([np.inf, np.nan, -np.inf])
    print(arr)
    print(np.isinf(arr))


if __name__ == "__main__":
    main()
