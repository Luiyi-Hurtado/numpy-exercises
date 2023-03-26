#!/usr/bin/python3
"""
Fucntion to get the numpy version and show
numpy build configuration
"""


import numpy as np


def main():
    """
    with this function get information from
    the version and configuration of numpy

    Args:
        Nothing

    Return:
        string
            the version and configuration of
            numpy
    """
    print(np.__version__)
    print(np.show_config())


if __name__ == "__main__":
    main()
