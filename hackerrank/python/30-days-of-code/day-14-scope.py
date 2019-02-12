"""
@author: acfromspace
"""


class Difference:

    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        # this is a game changer of creating functions within functions
        self.maximumDifference = max(a) - min(a)


# End of Difference class

# _ = input("Input amount of numbers to be compared: ") # this doesn't really matter
a = [int(e) for e in input("Input the numbers to be compared: ").split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
