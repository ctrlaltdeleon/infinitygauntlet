"""
@author: acfromspace
"""

import numpy

if __name__ == "__main__":

    # Only required to complete hackerrank challenge
    numpy.set_printoptions(sign=' ')

    # Take string, turn into floats into an array
    data = numpy.array(
        input("Input string with numbers separated: ").split(), float)

    print(numpy.floor(data))
    print(numpy.ceil(data))
    print(numpy.rint(data))
