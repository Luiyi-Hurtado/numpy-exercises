#!/usr/bin/python3
"""
Function to get help on the add function
"""


import numpy as np


def main():
    """
    This script get the information above
    the add function, using the help function

    Args.
        Nothing

    Returns:
        string:
            how to use a function
    """
    print(np.info(np.add))


if __name__ == "__main__":
    main()
