class Difference:
    def __init__(self, a):
        self.__elements = a

    def compute_difference(self):
        self.maximumDifference = max(a) - min(a)

a = [int(e) for e in input("Input the numbers to be compared: ").split(' ')]
d = Difference(a)
d.compute_difference()
print(d.maximumDifference)

"""
Input the numbers to be compared: 20 100
80
"""